from typing import List
from .types import User
from src.internals.database.database import get_raw_conn, return_conn
from src.internals.utils.logger import log
from src.lib.artist import is_artist_dnp
# from .comments import import_comments
from development.types import Extended_Random
from development.internals import dev_random
from .randoms import random_user
from .posts import import_posts
from .dms import import_dms


def import_users(import_id: str, key: str, contributor_id: str, random: Extended_Random = dev_random):
    """Imports test users."""
    user_amount = range(random.randint(3, 15))
    users: List[User] = [random_user() for user in user_amount]
    log(import_id, f"{len(users)} creators are going to be \"imported\"")

    if users:
        for user in users:
            log(import_id, f"Importing user \"{user['id']}\"")
            import_user(import_id, key, user, contributor_id)
        log(import_id, "Finished importing users")

    else:
        log(import_id, "User not supplied. Will not be imported.")


def import_user(import_id: str, key: str, user: User, contributor_id: str):
    """Imports a test user."""

    if is_artist_dnp('kemono-dev', user['id']):
        log(import_id, f"Skipping user {user['id']} because they are in do not post list")
        return

    import_posts(import_id, key, contributor_id, user_id=user['id'])
    import_dms(import_id, key, contributor_id, user_id=user['id'])
    # import_comments(import_id, key, user)
    try:
        save_user_to_db(user)
        log(import_id, f"Finished importing creator {user['id']}")
    except Exception as e:
        log(import_id, f"ERROR {e}: FAILED TO IMPORT {user}")


def save_user_to_db(user: User):
    columns = user.keys()
    values = ['%s'] * len(user.values())
    query = """
    INSERT INTO lookup ({fields})
    VALUES ({values})
    ON CONFLICT (id, service)
    DO NOTHING""".format(
        fields=','.join(columns),
        values=','.join(values)
    )

    conn = get_raw_conn()
    try:
        cursor = conn.cursor()
        cursor.execute(query, list(user.values()))
        conn.commit()
    finally:
        return_conn(conn)
