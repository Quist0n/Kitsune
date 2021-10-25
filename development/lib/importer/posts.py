import sys
import json

from src.internals.utils.logger import log
from development.internals.database import query_db

from typing import List
from .types import Post, File
sys.setrecursionlimit(100000)


def import_posts(import_id: str, posts: List[Post]):
    """Imports test posts."""

    log(import_id, f'{len(posts)} posts are going to be \"imported\".')

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
        ON CONFLICT (id, service)
            DO NOTHING
    """
    query_db(query, query_params)


def get_files_from_posts(posts: List[Post]) -> List[File]:
    """
    A helper function to create a single collection out of all files from posts.
    """
    files = []

    for post in posts:
        file = post['file'] if post['file'].get('name') else None
        attachments = post['attachments'] if post.get('attachments') else None
        inner_files = []

        if file:
            inner_files.append(file)

        if attachments:
            inner_files.extend(attachments)

        if inner_files:
            files.extend(inner_files)

    return files
