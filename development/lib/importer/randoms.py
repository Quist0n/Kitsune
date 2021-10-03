from datetime import datetime
from development.internals.random import Custom_Random
from development.internals.importer import service_name

from .types import Post, User, DM, Comment, Embed, File, Attachment

max_date = '' # ISO timestamp
seed = 'seed'
test_random = Custom_Random(seed)

def random_post() -> Post:
    post = Post(
        id= test_random.string(0, 255),
        user_id= test_random.string(0, 255),
        service= service_name,
        title= test_random.lorem_ipsum(1, 1),
        content= test_random.lorem_ipsum(1, 5),
        embed= random_embed(),
        shared_file= test_random.boolean(),
        file= random_file(),
        attachments= [random_attachment() for attachment in range(1, test_random.randint(1, 50))]
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
