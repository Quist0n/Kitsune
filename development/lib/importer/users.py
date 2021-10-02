from src.internals.utils.logger import log
from src.lib.artist import is_artist_dnp
from .comments import import_comments

from typing import List
from .types import User

def import_users(import_id: str, key: str):
    """Imports test users."""
    users: List[User] = []

    for user in users:
        import_user(import_id, key, user)


def import_user(import_id: str, key: str, user: User):
    """Imports a test user."""

    if is_artist_dnp('kemono-dev', user['id']):
        log(import_id, f"Skipping user {user['id']} because they are in do not post list")
        return

    import_comments(import_id, key, user)
    log(import_id, f"Starting import: {user['id']} from user {user['id']}")
