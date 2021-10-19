import sys
sys.setrecursionlimit(100000)
import json

from development.internals import dev_random
from src.internals.database.database import get_raw_conn, return_conn from src.internals.utils.logger import log
from src.lib.post import post_exists, post_flagged
from src.importers.patreon import get_current_user_id
from .randoms import random_post
from .dms import import_dms
from development.types import Extended_Random

from typing import List
from .types import Post

def import_posts(import_id: str, key: str, contributor_id: str, random: Extended_Random = dev_random):
    """Imports test posts with dms."""

    log(import_id, f"Importing DMs...")
    import_dms(import_id, key, contributor_id)
    log(import_id, f"Done importing DMs.")

    post_amount = range(random.randint(23, 117))
    posts: List[Post] = [random_post(random) for post in post_amount]
    log(import_id, f'{len(posts)} posts are going to be \"imported\".')

    for post in posts:
        log(import_id, f"Importing post \"{post['id']}\" from artist \"{post['user']}\".")
        import_post(import_id, key, post)

    log(import_id, f"Finished scanning for posts")

def import_post(import_id:str, key: str, post: Post):
    """Imports a single test post."""

    # if post_exists('kemono-dev', post['user'], post['id']) and not post_flagged('kemono-dev', post['user'], post['id']):
    #     log(import_id, f"Skipping post \"{post['id']}\" from user because already exists.")
    #     return

    log(import_id, f"Starting import: \"{post['id']}\" from user \"{post['user']}\"")
    save_post_to_db(post)

def save_post_to_db(post: Post):
    """
    Saves test posts to DB.
    TODO: rewrite into more generic way.
    """
    query_params = dict(
        id = post['id'],
        user = post['user'],
        service = post['service'],
        file = json.dumps(post['file']),
        attachments = [json.dumps(post['attachments'])],
    )

    query = """
    INSERT INTO posts (id, \"user\", service, file, attachments)
    VALUES (%(id)s, %(user)s, %(service)s, %(file)s, %(attachments)s::jsonb[])
    ON CONFLICT (id, service) DO NOTHING
    """

    try:
        conn = get_raw_conn()
        cursor = conn.cursor()
        cursor.execute(query, query_params)
        cursor.close()
        conn.commit()
    finally:
        return_conn(conn)
