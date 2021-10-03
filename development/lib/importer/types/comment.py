from datetime import datetime
from typing import TypedDict

class Optional(TypedDict, total= False):
    parent_id: str
    added: datetime

class Comment():
    id: str
    post_id: str
    parent_id: str
    commenter: str
    service: str
    content: str
    published: datetime
