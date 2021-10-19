from development.internals import service_name, dev_random
from development.types import Extended_Random

from .types import Post, User, DM, File, Attachment

def random_post(random: Extended_Random = dev_random) -> Post:
    post = Post(
        id = random.string(5, 25),
        user = random.string(5, 25),
        service = service_name,
        attachments = [random_attachment() for i in range(random.randint(0, 7))],
        file = random_file(),
    )
    return post

def random_user(random: Extended_Random = dev_random) -> User:
    user = User(
        id = random.string(5, 25),
        service = service_name,
    )

    return user


def random_dm(random: Extended_Random = dev_random) -> DM:
    """Generates a random DM"""
    dm = DM(
        id = random.string(5,25),
        user = random.string(5,25),
        service = service_name,
        file = random_file(),
    )
    return dm


def random_file(random: Extended_Random = dev_random) -> File:
    random_file_name = f"{random.string(8, 32)}.{random.string(1,5)}"
    path = f"/assests/{random_file_name}"

    file = File(
        name = random_file_name,
        path = path,
    )

    return file

def random_attachment(random: Extended_Random = dev_random) -> Attachment:
    file = random_file()
    attachment = Attachment(
        name = file.get('name'),
        path = file.get('path'),
        )

    return attachment
