from .types import Post
from development.types import Extended_Random
from .randoms import random_post, random_user, random_dm
from .users import import_users
from .dms import import_dms
from development.internals.database import query_db
from src.internals.utils.logger import log
from src.internals.database.database import get_raw_conn, return_conn
from development.internals import dev_random
import json
import sys
sys.setrecursionlimit(100000)


def import_posts(import_id: str, key: str, contributor_id: str, random: Extended_Random = dev_random):
    """Imports test posts with dms."""
    user_amount = range(random.randint(3, 15))
    users = [random_user() for user in user_amount]
    log(import_id, f"{len(users)} creators are going to be \"imported\"")
    post_users = random.sample(users, random.randint(1, len(users)))
    dm_users = random.sample(users, random.randint(1, len(users)))

    post_amount = range(random.randint(23, 117))
    posts = [random_post(random=random) for index in post_amount]
    posts.extend([random_post(user['id'], random) for user in post_users])
    log(import_id, f'{len(posts)} posts are going to be \"imported\".')

    dm_amount = range(random.randint(7, 13))
    dms = [random_dm(import_id, contributor_id, random=random) for index in dm_amount]
    dms.extend([random_dm(import_id, contributor_id, user['id'], random) for user in dm_users])
    log(import_id, f'{len(dms)} DMs are going to be \"imported\"')

    import_dms(import_id, dms)
    import_users(import_id, users)

    for post in posts:
        log(import_id, f"Importing post \"{post['id']}\" from user \"{post['user']}\".")
        import_post(import_id, post)

    log(import_id, "Done importing posts.")


def import_post(import_id: str, post: Post):
    """Imports a single test post."""

    # if post_exists('kemono-dev', post['user'], post['id']) and not post_flagged('kemono-dev', post['user'], post['id']):
    #     log(import_id, f"Skipping post \"{post['id']}\" from user because already exists.")
    #     return

    try:
        save_post_to_db(post)
    except Exception as e:
        log(import_id, f"ERROR {e}: FAILED TO IMPORT {post}")


def save_post_to_db(post: Post):
    """
    Saves test posts to DB.
    TODO: rewrite into more generic way.
    """
    query_params = dict(
        id=post['id'],
        user=post['user'],
        service=post['service'],
        file=json.dumps(post['file']),
        attachments=[json.dumps(attachment) for attachment in post['attachments']],
        published=post['published'],
        edited=post['edited'],
        title=post['title'],
        content=post['content']
    )

    query = """
        INSERT INTO posts
            (id, \"user\", service, file, attachments, published, edited, title, content)
        VALUES (%(id)s, %(user)s, %(service)s, %(file)s, %(attachments)s::jsonb[], %(published)s, %(edited)s, %(title)s, %(content)s)
        ON CONFLICT (id, service) DO NOTHING
    """
    query_db(query, query_params)
