from pathlib import Path

from typing import List


def get_folder_file_paths(folder: Path, extensions: List[str] = None) -> List[Path]:
    """
    Reads the folder shallowly at provided absolute path.
    Returns a list of absolute paths for files inside it.
    If the list of extensions provided,
    limit the resulting list to the files with these exntesions
    """
    if not folder.is_absolute():
        raise ValueError(f'Path "{folder}" is not absolute.')

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
