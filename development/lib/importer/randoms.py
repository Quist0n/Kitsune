from development.internals import service_name, dev_random, file_extensions
from development.types import Extended_Random

from .types import Post, User, DM, File, Attachment


def random_post(user_id: str = None, random: Extended_Random = dev_random) -> Post:
    post = Post(
        id=random.string(5, 25),
        user=user_id if user_id else random.string(5, 25),
        service=service_name,
        attachments=[random_attachment() for i in range(random.randint(0, 54))],
        file=random_file(),
    )
    return post


def random_user(random: Extended_Random = dev_random) -> User:
    user = User(
        id=random.string(5, 25),
        name=random.string(5, 25),
        service=service_name,
    )

    return user


def random_dm(import_id: str, contributor_id: str, user_id: str = None, random: Extended_Random = dev_random) -> DM:
    """Generates a random DM"""
    dm = DM(
        import_id=import_id,
        id=random.string(5, 25),
        contributor_id=contributor_id,
        user=user_id if user_id else random.string(5, 25),
        service=service_name,
        file=random_file(),
        published=random.date()
    )
    return dm


def random_file(random: Extended_Random = dev_random) -> File:
    random_file_name = f"{random.string(8, 32)}.{random.choice(file_extensions)}"
    path = f"/assests/{random_file_name}"

    file = File(
        name=random_file_name,
        path=path,
    )

    return file


def random_attachment(random: Extended_Random = dev_random) -> Attachment:
    file = random_file()
    attachment = Attachment(
        name=file.get('name'),
        path=file.get('path'),
    )

    return attachment
