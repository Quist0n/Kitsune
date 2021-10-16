from development.internals import service_name
from development.types import Extended_Random

from .types import Post, User, DM, Comment, Embed, File, Attachment


seed = 'Kitsune_Sneedy_Seed'
test_random = Extended_Random(seed)


def random_post() -> Post:
    post = Post(
        id = test_random.string(0, 255),
        user_id = test_random.string(0, 255),
        service = service_name
    )
    return post


def random_user() -> User:
    user = User(
            id = test_random.string(0, 255),
        service = service_name

    )
    return user


def random_dm() -> DM:
    dm = DM(
            id = test_random.string(0, 255),
            user_id = test_random.string(0, 255),
            service = service_name,
            content = test_random.string(0, 128),
            embed = random_embed(),
            file = random_file(),
            published = test_random.date(),
    )

    return dm


def random_comment() -> Comment:
    pass


def random_embed() -> Embed:
    embed = Embed(

    )
    return embed


def random_file() -> File:
    file = File()
    return file


def random_attachment() -> Attachment:
    attachment = Attachment()
    return attachment
