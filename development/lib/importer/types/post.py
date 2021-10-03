from datetime import datetime

from typing import TypedDict, List
from .attachment import Attachment
from .embed import Embed
from .file import File

class Optional(TypedDict, total= False):
    added: datetime
    published: datetime
    edited: datetime

class Post(Optional):
    id: str
    user_id: str
    service: str
    title: str
    content: str
    embed: Embed
    shared_file: bool
    file: File
    attachments: List[Attachment]
