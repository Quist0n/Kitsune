from datetime import datetime
from typing import TypedDict

from .embed import Embed
from .file import File

class Optional(TypedDict, total= False):
    added: datetime
    import_id: str
    contributor_id: str
    content: str
    embed: Embed
    published: datetime

class DM(Optional):
    id: str
    user: str
    service: str
    file: File
