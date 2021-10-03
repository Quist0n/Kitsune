from datetime import datetime
from typing import TypedDict

class Optional(TypedDict, total= False):
    password_hash: str
    created_at: datetime

class Account(Optional):
    id: int
    username: str
