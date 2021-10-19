import sys
sys.setrecursionlimit(100000)
import json

from development.internals import dev_random
from src.internals.database.database import get_raw_conn, return_conn
from src.internals.utils.logger import log

from .randoms import random_dm
from development.types import Extended_Random

from typing import List
from .types import DM


def import_dms(import_id: str, key: str, contributor_id: str, random: Extended_Random = dev_random):
    """Imports test DMs."""

    try:
        dm_amount = range(random.randint(2, 90))
        dms: List[DM] = [random_dm(random) for i in dm_amount]
    except Exception as e:
        log(import_id, f"Error:{e}")

    log(import_id, f'{len(dms)} DMs are going to be \"imported\"')

    for dm in dms:
            log(import_id, f"Importing dm {dm['id']}")
            import_dm(import_id, key, contributor_id, dm)



def import_dm(import_id: str, key: str, contributor_id: str, dm: DM):
    """Imports a single test DM"""
    log(import_id, f"Starting import: {dm['id']} from user")
    try:
        save_dm_to_db(dm)
    except Exception as e:
        log(import_id, f"Error:{e} with dm: {dm}")


def save_dm_to_db(dm: DM):
    """Save test dm to DB"""
    query_params = dict(
        id = dm['id'],
        user = dm['user'],
        service = dm['service'],
        file = json.dumps(dm['file']),
    )

    print("Query params:\n", query_params)
    print("dm info:\n", dm)
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
