from src.internals.utils.logger import log
from src.lib.artist import is_artist_dnp
from .comments import import_comments

from typing import List
from .types import User

def import_users(import_id: str, key: str):
    """Imports test users."""
    user_amount = range(test_random.randint(23, 117))
    users: List[User] = [ random_user() for user in user_amount ]

    if users
        for user in users:
            log(import_id, f"Importing user {user['id']}")
            import_user(import_id, key, user)

    else:
        log(import_id, f"User not supplied. Will not be imported."))
def import_user(import_id: str, key: str, user: User):
    """Imports a test user."""

    if is_artist_dnp('kemono-dev', user['id']):
        log(import_id, f"Skipping user {user['id']} because they are in do not post list")
        return

    import_comments(import_id, key, user)
    log(import_id, f"Starting import: {user['id']} from user {user['id']}")
    save_user_to_db(user)

def save_user_to_db(user: User):
    query_args = dict(
    fields = ",".join(user.keys()),
    values = ",".join(user.values()),
    )

    query = """
        INSERT INTO lookup (%(fields)s)
        VALUES (%(values)s)
        ON CONFLICT (id, service)
            DO NOTHING;
    """

    conn = get_raw_conn()

    try:
        cursor = conn.cursor()
        cursor.execute(query, query_args)
        conn.commit()
    finally:
        return_conn(conn)
