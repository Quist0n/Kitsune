import os
import tempfile
import shutil
from pathlib import Path
from uuid import uuid4
from datetime import datetime

from configs.derived_vars import temp_dir_root, data_folder
from src.internals.utils.utils import get_hash_of_file
from development.types.models import File, File_Meta

from typing import List


def get_folder_file_paths(folder: Path, extensions: List[str] = None) -> List[Path]:
    """
    Reads the folder shallowly at provided absolute path.
    Returns a list of absolute paths for files inside it.
    If the list of extensions provided,
    limits the resulting list to the files with these extensions.
    """
    if not folder.is_absolute():
        raise ValueError(f'Path "{folder}" is not absolute.')

    if not folder.is_dir():
        raise ValueError(f'Path "{folder}" is not a folder.')

    files = []
    if not extensions:
        for path in folder.iterdir():
            if path.is_file():
                files.append(path)
                continue
    else:
        for path in folder.iterdir():
            if path.is_file() and path.suffix and path.suffix[1:] in extensions:
                files.append(path)
                continue

    return files


def get_file_from_path(file_path: Path):
    """
    Gets the file out of provided absolute path.
    """
    temp_path = create_temporary_directory()
    hash_filename = generate_hashy_filename(temp_path)
    file_name = temp_dir_root.joinpath(temp_path.name)
    mtime = datetime.fromtimestamp(file_name.stat().st_mtime)
    ctime = datetime.fromtimestamp(file_name.stat().st_mtime)
    real_path = Path(data_folder, hash_filename)

    if real_path.exists():
        shutil.rmtree(temp_path.parent, ignore_errors=True)
        return (Path(temp_path.name, hash_filename), file_path)

    file = File(
        mtime=mtime,
        ctime=ctime
    )
    return file


def create_temporary_directory() -> Path:
    """"""
    os.makedirs(temp_dir_root, exist_ok=True)
    temp_dir = tempfile.mkdtemp(dir=temp_dir_root)
    temp_name = f'{str(uuid4())}.temp'
    temp_path = Path(temp_dir, temp_name)
    return temp_path


def generate_hashy_filename(file_path: Path):
    """
    Generates unique filename.
    """
    file_hash = get_hash_of_file(file_path)
    hash_filename = Path(file_hash[0:2], file_hash[2:4], file_hash + file_path.suffix)
    return hash_filename
