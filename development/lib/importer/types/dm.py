from datetime import datetime
from typing import TypedDict

from .embed import Embed
from .file import File

class Optional(TypedDict, total= False):
    added: datetime
    import_id: str
    contributor_id: str

class DM(Optional):
    id: str
    user_id:str
    service: str
    content: str
    embed: Embed
    published: datetime
    file: File
