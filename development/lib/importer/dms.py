import sys
import json
from development.internals import dev_random
from src.internals.database.database import get_raw_conn, return_conn
from src.internals.utils.logger import log
from .randoms import random_dm
from development.types import Extended_Random
from typing import List
from .types import DM
sys.setrecursionlimit(100000)


def import_dms(import_id: str, key: str, contributor_id: str, random: Extended_Random = dev_random, user_id: str = None):
    """Imports test DMs."""

    log(import_id, "Importing DMs...")
    dm_amount = range(random.randint(2, 90))
    dms: List[DM] = [random_dm(random, user_id) for i in dm_amount]

    log(import_id, f'{len(dms)} DMs are going to be \"imported\"')

    for dm in dms:
        log(import_id, f"Importing dm \"{dm['id']}\" from user \"{dm['user']}\"")
        import_dm(import_id, key, contributor_id, dm)

    log(import_id, "Done importing DMs.")


def import_dm(import_id: str, key: str, contributor_id: str, dm: DM):
    """Imports a single test DM"""
    try:
        save_dm_to_db(dm)
    except Exception as e:
        log(import_id, f"ERROR {e}: FAILED TO IMPORT {dm}")


def save_dm_to_db(dm: DM):
    """Save test dm to DB"""
    query_params = dict(
        id=dm['id'],
        user=dm['user'],
        service=dm['service'],
        file=json.dumps(dm['file']),
    )

    query = """
    INSERT INTO dms (id, \"user\", service, file)
    VALUES (%(id)s, %(user)s, %(service)s, %(file)s)
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
