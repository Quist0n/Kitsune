from psycopg2.extensions import connection

from src.internals.database.database import get_raw_conn, return_conn
from development.internals.database import query_db_without_commit

from typing import Union
from development.types.models import File, File_Meta, Discord_File_Meta


def save_file_to_server():
    """
    TODO: complete it
    """
    remote_path = None
    file_model = File()
    file_meta = File_Meta()
    is_discord = False
    save_file_data_to_db(remote_path, file_model, file_meta, is_discord)


def save_file_data_to_db(remote_path: str, file_model: File, file_meta: Union[File_Meta, Discord_File_Meta], is_discord=False):
    """
    Saves the file data to a database.
    """
    conn = get_raw_conn()

    file_id = save_file_info_to_db(conn, file_model)

    if is_discord:
        save_discord_file_meta_to_db(conn, file_id, file_meta)
    else:
        save_file_meta_to_db(conn, file_id, file_meta)

    save_file_relations_to_db(file_id, remote_path)
    conn.commit()
    return_conn(conn)


def save_file_info_to_db(conn: connection, file_model: File) -> int:
    """
    Saves the file info to a database.
    """
    query_args = dict(
        hash=file_model['hash'],
        mtime=file_model['mtime'],
        ctime=file_model['ctime'],
        mime=file_model['mime'],
        ext=file_model['ext'],
    )
    query = """
        INSERT INTO files
            (hash, mtime, ctime, mime, ext)
        VALUES (%(hash)s, %(mtime)s, %(ctime)s, %(mime)s, %(ext)s)
        ON CONFLICT (hash)
            DO UPDATE
                SET hash = EXCLUDED.hash
        RETURNING id
    """
    cursor = conn.cursor()
    cursor.execute(query, query_args)
    file_id: int = cursor.fetchone()['id']

    return file_id


def save_file_meta_to_db(conn: connection, file_id: int, file_meta: File_Meta):
    """
    Saves the file metadata to a database.
    """
    query_args = dict(
        file_id=file_id,
        filename=file_meta['filename'],
        service=file_meta['service'],
        user=file_meta['user'],
        post=file_meta['post'],
        inline=file_meta['inline']
    )
    query = """
        INSERT INTO file_post_relationships
            (file_id, filename, service, \"user\", post, inline)
        VALUES (%(file_id)s, %(filename)s, %(service)s, %(user)s, %(post)s, %(inline)s)
        ON CONFLICT DO NOTHING
    """
    query_db_without_commit(conn, query, query_args)


def save_discord_file_meta_to_db(conn: connection, file_id: int, discord_file_meta: Discord_File_Meta):
    """
    Saves the discord file metadata to a database.
    """
    query_args = dict(
        file_id=file_id,
        filename=discord_file_meta['filename'],
        server=discord_file_meta['server'],
        channel=discord_file_meta['channel'],
        id=discord_file_meta['id']
    )
    query = """
        INSERT INTO file_discord_message_relationships
            (file_id, filename, server, channel, id)
        VALUES (%(file_id)s, %(filename)s, %(server)s, %(channel)s, %(id)s)
        ON CONFLICT DO NOTHING
    """
    query_db_without_commit(conn, query, query_args)


def save_file_relations_to_db(conn: connection, file_id: str, remote_path: str):
    """"""
    query_args = dict(
        file_id=file_id,
        remote_path=remote_path
    )
    query = """
        INSERT INTO file_server_relationships
            (file_id, remote_path)
        VALUES (%(file_id)s, %(remote_path)s)
    """
    query_db_without_commit(conn, query, query_args)
