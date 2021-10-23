from .base import Database_Model


class File(Database_Model):
    hash: str
    mtime: str
    ctime: str
    mime: str
    ext: str


class Meta(Database_Model):
    filename: str


class File_Meta(Meta):
    service: str
    user: str
    post: str
    inline: bool


class Discord_File_Meta(Meta):
    server: str
    channel: str
    id: str
