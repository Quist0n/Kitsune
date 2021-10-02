from datetime import datetime

from typing import TypedDict, List
from .attachment import Attachment
from .embed import Embed
from .file import File

class Post(TypedDict):
    id: str
    user_id: str
    service: str
    title: str
    content: str
    embed: Embed
    shared_file: bool
    added: datetime
    published: str
    edited: str
    file: File
    attachments: List[Attachment]
