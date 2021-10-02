from src.importers.patreon import get_current_user_id

from typing import List
from .types import DM

def import_dms(import_id: str, key: str, contributor_id: str):
    current_user_id = get_current_user_id(key, import_id)
    dms: List[DM] = []
    """Imports test DMs."""
    pass
