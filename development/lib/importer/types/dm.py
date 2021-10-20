from datetime import datetime
from typing import TypedDict

from .embed import Embed
from .file import File


class Optional(TypedDict, total=False):
    added: datetime
    content: str
    embed: Embed


class DM(Optional):
    id: str
    import_id: str
    contributor_id: str
    published: datetime
    user: str
    service: str
    file: File
