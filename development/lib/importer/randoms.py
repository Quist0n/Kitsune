from development import service_name
from development.types import Extended_Random

from .types import Post, User, DM, Comment, Embed, File, Attachment

max_date = '' # ISO timestamp
seed = 'seed'
test_random = Extended_Random(seed)

def random_post() -> Post:
    post = Post(
        id= test_random.string(0, 255),
        user_id= test_random.string(0, 255),
        service= service_name,
    )
    return post


def random_user() -> User:
    pass


def random_dm() -> DM:
    pass


def random_comment() -> Comment:
    pass

def random_embed() -> Embed:
    embed = Embed()
    return embed

def random_file() -> File:
    file = File()
    return file

def random_attachment() -> Attachment:
    attachment = Attachment()
    return attachment
