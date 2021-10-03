from datetime import datetime
from typing import TypedDict

class Optional(TypedDict, total= False):
    indexed: datetime
    updated: datetime

class User(Optional):
    id: str
    name: str
    service: str
