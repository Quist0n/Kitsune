import sys
import json
from typing import List
from .types import Post
from development.internals import dev_random
from src.internals.database.database import get_raw_conn, return_conn
from src.internals.utils.logger import log
from .randoms import random_post
from development.types import Extended_Random
sys.setrecursionlimit(100000)


def import_posts(import_id: str, key: str, contributor_id: str, random: Extended_Random = dev_random, user_id: str = None):
    """Imports test posts with dms."""

    post_amount = range(random.randint(23, 117))
    posts: List[Post] = [random_post(random, user_id) for post in post_amount]
    log(import_id, f'{len(posts)} posts are going to be \"imported\".')

    for post in posts:
        log(import_id, f"Importing post \"{post['id']}\" from user \"{post['user']}\".")
        import_post(import_id, key, post)

    log(import_id, "Done importing posts.")


def import_post(import_id: str, key: str, post: Post):
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
        attachments=[json.dumps(post['attachments'])],
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
