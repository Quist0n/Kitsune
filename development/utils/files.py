from pathlib import Path

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


def get_file_from_path(path: Path):
    """
    Gets the file out of provided absolute path.
    """
    file = None
    return file


def uniquify_filename(path: Path):
    new_filename = None
    return new_filename
