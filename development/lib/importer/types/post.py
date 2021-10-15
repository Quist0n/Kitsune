from datetime import datetime

from typing import TypedDict, List
from .attachment import Attachment
from .embed import Embed
from .file import File

class Post_Model(TypedDict):
    id: str
    user: str
    service: str

class Optional(TypedDict, total= False):
    added: datetime
    published: datetime
    edited: datetime
    embed: Embed
    shared_file: bool
    title: str
    content: str

class Post(Optional):
    id: str
    user_id: str
    service: str
    file: File
    attachments: List[Attachment]
