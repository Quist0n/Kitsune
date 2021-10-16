import sys
sys.setrecursionlimit(100000)

from development.internals import dev_random
from src.internals.database.database import get_raw_conn, return_conn
from src.internals.utils.logger import log
from src.lib.post import post_exists, post_flagged
from .randoms import random_post

from typing import List
from development.types import Extended_Random
from .types import Post

def import_posts(import_id: str, key: str, random: Extended_Random = dev_random):
    """Imports test posts."""

    post_amount = range(random.randint(23, 117))
    posts: List[Post] = [random_post(random) for post in post_amount]
    log(import_id, f"{len(posts)} posts are going to be \"imported\"")

    for post in posts:
        log(import_id, f"Importing post {post['id']}")
        import_post(import_id, key, post)

def import_post(import_id:str, key: str, post: Post):
    """Imports a test post."""

    # if post_exists('kemono-dev', post['user'], post['id']) and not post_flagged('kemono-dev', post['user'], post['id']):
    #     log(import_id, f"Skipping post \"{post['id']}\" from user because already exists.")
    #     return

    log(import_id, f"Starting import: {post['id']} from user")
    save_post_to_db(post)

def save_post_to_db(post: Post):
    query = f"""
        INSERT INTO posts ({','.join(post.keys())})
        VALUES ({ ','.join(post.values()) })
        ON CONFLICT (id, service)
            DO NOTHING
    """
    conn = get_raw_conn()

    try:
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
    finally:
        return_conn(conn)
