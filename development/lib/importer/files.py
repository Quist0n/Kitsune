import os
import shutil
import magic
from pathlib import Path
from datetime import datetime

from configs.derived_vars import data_folder
from src.internals.utils.download import make_thumbnail
from src.internals.utils.logger import log
from src.lib.files import write_file_log
from development.internals import service_name
from development.utils import create_temporary_directory, generate_hashy_filename

from typing import List
from development.types.models import File as File_Model, File_Meta
from .types import File


def import_files(import_id: str, files: List[File]):
    """"""
    log(import_id, f'{len(files)} files are going to be \"imported\".')

    for file in files:
        log(import_id,
            f'Importing file \"{file["name"]}\" from the post \"{file["post"]}\" by user \"{file["user"]}\".')
        file_model = get_file_model(file['path'])
        file_meta = File_Meta(
            filename=file['name'],
            post=file['post'],
            service=service_name,
            user=file['user'],
        )
        import_file(file_model, file_meta)

    log(import_id, "Done importing files.")


def import_file(file: File_Model, file_meta: File_Meta):
    """"""
    write_file_log(
        fhash=file['hash'],
        mtime=file['mtime'],
        ctime=file['ctime'],
        mime=file['mime'],
        ext=file['ext'],
        filename=file_meta['filename'],
        service=file_meta['service'],
        user=file_meta['user'],
        post=file_meta['post'],
        remote_path=""
    )


def get_file_model(file_path: Path):
    """
    Gets the file out of provided absolute path.
    """
    temp_path = create_temporary_directory()
    hash_filename = generate_hashy_filename(temp_path)
    mtime = datetime.fromtimestamp(temp_path.stat().st_mtime)
    ctime = datetime.fromtimestamp(temp_path.stat().st_ctime)
    mime = magic.from_file(temp_path, mime=True)
    file_model = File(
        hash=hash_filename.stem,
        filename=file_path.name,
        mtime=mtime,
        ctime=ctime,
        mime=mime,
        ext=hash_filename.suffix,
    )
    real_path = Path(data_folder, hash_filename)

    if not real_path.exists():
        os.makedirs(real_path, exist_ok=True)
        os.rename(temp_path, real_path)

    shutil.rmtree(temp_path.parent, ignore_errors=True)
    make_thumbnail(real_path)

    return file_model
