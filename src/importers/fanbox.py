import sys
sys.path.append('./PixivUtil2')
sys.setrecursionlimit(100000)

from os import makedirs
from os.path import join
import requests
import datetime
import config
import json

from flask import current_app

from ...PixivUtil2.PixivModelFanbox import FanboxArtist, FanboxPost

from ..internals.database.database import get_conn
from ..lib.artist import index_artists, is_artist_dnp
from ..lib.post import remove_post_if_flagged_for_reimport, post_exists
from ..lib.proxy import get_proxy
from ..lib.download import download_file, DownloaderException
from ..internals.utils.utils import get_import_id
from ..internals.utils.logger import log

def import_posts(import_id, key, url = 'https://api.fanbox.cc/post.listSupporting?limit=50'):
    makedirs(join(config.download_path, 'logs'), exist_ok=True)

    try:
        scraper = requests.get(
            url,
            cookies={ 'FANBOXSESSID': key },
            headers={ 'origin': 'https://fanbox.cc' },
            proxies=get_proxy()
        )
        scraper_data = scraper.json()
    except requests.HTTPError:
        log(f'[{import_id}]: HTTP error when contacting Fanbox API ({url}). Stopping import.', 'exception', True)
        return

    conn = get_conn()
    user_id = None
    posts_imported = []
    artists_with_posts_imported = []
    if scraper_data.get('body'):
        for post in scraper_data['body']['items']:
            user_id = post['user']['userId']
            post_id = post['id']

            parsed_post = FanboxPost(post_id, None, post)
            if parsed_post.is_restricted:
                log(f'[{import_id}]: Skipping post {post_id} from user {user_id} because restricted')
                continue
            try:
                file_directory = f"files/fanbox/{user_id}/{post_id}"
                attachments_directory = f"attachments/fanbox/{user_id}/{post_id}"

                if is_artist_dnp('fanbox', user_id):
                    log(f"[{import_id}]: Skipping post {post_id} from user {user_id} is in do not post list")
                    continue

                remove_post_if_flagged_for_reimport('fanbox', user_id, post_id)

                if post_exists('fanbox', user_id, post_id):
                    log(f'[{import_id}]: Skipping post {post_id} from user {user_id} because already exists', to_client = True)
                    continue

                log(f"[{import_id}]: Starting import: {post_id} from user {user_id}", to_client = True)

                post_model = {
                    'id': post_id,
                    '"user"': user_id,
                    'service': 'fanbox',
                    'title': post['title'],
                    'content': parsed_post.body_text,
                    'embed': {},
                    'shared_file': False,
                    'added': datetime.datetime.now(),
                    'published': post['publishedDatetime'],
                    'edited': post['updatedDatetime'],
                    'file': {},
                    'attachments': []
                }

                for i in range(len(parsed_post.embeddedFiles)):
                    if i == 0:
                        filename, _ = download_file(
                            join(config.download_path, file_directory),
                            parsed_post.embeddedFiles[i],
                            cookies={ 'FANBOXSESSID': key },
                            headers={ 'origin': 'https://fanbox.cc' }
                        )
                        post_model['file']['name'] = filename
                        post_model['file']['path'] = f'/{file_directory}/{filename}'
                    else:
                        filename, _ = download_file(
                            join(config.download_path, attachments_directory),
                            parsed_post.embeddedFiles[i],
                            cookies={ 'FANBOXSESSID': key },
                            headers={ 'origin': 'https://fanbox.cc' }
                        )
                        post_model['attachments'].append({
                            'name': filename,
                            'path': f'/{attachments_directory}/{filename}'
                        })

                post_model['embed'] = json.dumps(post_model['embed'])
                post_model['file'] = json.dumps(post_model['file'])
                for i in range(len(post_model['attachments'])):
                    post_model['attachments'][i] = json.dumps(post_model['attachments'][i])

                columns = post_model.keys()
                data = ['%s'] * len(post_model.values())
                data[-1] = '%s::jsonb[]' # attachments
                query = "INSERT INTO posts ({fields}) VALUES ({values})".format(
                    fields = ','.join(columns),
                    values = ','.join(data)
                )
                cursor = conn.cursor()
                cursor.execute(query, list(post_model.values()))
                conn.commit()

                log(f'[{import_id}]: Finished importing {post_id} for user {user_id}')
            except Exception as e:
                log(f'[{import_id}]: Error importing post {post_id} from user {user_id}', 'exception', True)
                conn.rollback()
                continue
        
        next_url = scraper_data['body'].get('nextUrl')
        if next_url:
            log(f'[{import_id}]: Finished processing page ({url}). Importing {next_url}', to_client = True)
            import_posts(log_id, key, next_url)
        else:
            log(current_app.logger.debug(f'[{import_id}]: Finished scanning for posts', to_client = True)
            index_artists()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        key = sys.argv[1]
        import_id = get_import_id(key)
        import_posts(import_id, sys.argv[1])
    else:
        print('Argument required - Login token')
