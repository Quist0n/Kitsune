from src.internals.database.database import get_raw_conn, return_conn
from src.internals.utils.logger import log
from src.lib.post import post_exists, post_flagged
from .dms import import_dms
from .randoms import random_post

from typing import List
from .types import Post

def import_posts(import_id: str, key: str, is_dms, contributor_id):
    """Imports test posts."""

    if (is_dms):
        log(import_id, f"Importing DMs...")
        import_dms(import_id, key, contributor_id)
        log(import_id, f"Done importing DMs.")

    posts: List[Post] = [random_post()]

    if posts:
        for post in posts:
            log(import_id, f"Importing post {post['id']}")
            import_post(import_id, key, post)
    else:
        log(import_id, f"No active subscriptions or invalid key. No posts will be imported.")

def import_post(import_id:str, key: str, post: Post):
    """Imports a test post."""

    if post_exists('kemono-dev', post['user_id'], post['id']) and not post_flagged('kemono-dev', post['user_id'], post['id']):
        log(import_id, f"Skipping post {post['id']} from user {post['user_id']} because already exists")
        return

    log(import_id, f"Starting import: {post['id']} from user {post['user_id']}")
    save_post_to_db(post)

def save_post_to_db(post: Post):
    query_args = dict(
        fields= ",".join(post.keys()),
        values= ",".join(post.values()),
    )
    query = """
        INSERT INTO posts (%(fields)s)
        VALUES (%(values)s)
        /*ON CONFLICT (id, service)
            DO UPDATE
                SET %(updates)s*/
    """
    conn = get_raw_conn()

    try:
        cursor = conn.cursor()
        cursor.execute(query, query_args)
        conn.commit()
    finally:
        return_conn(conn)
