# from pathlib import Path

from development.internals import service_name, dev_random, asset_files
from development.types import Extended_Random

from .types import Post, User, DM, File, Attachment


def random_post(user_id: str = None, random: Extended_Random = dev_random) -> Post:
    published_date = random.date() if random.boolean() else None
    edited_date = random.date(published_date) if published_date and random.boolean() else None
    title = random.lorem_ipsum(1, 1, 1) if random.boolean() else ''
    content = random.lorem_ipsum() if random.boolean() else ''
    attachments_amount = range(random.randint(0, 54))
    post = Post(
        id=random.string(5, 25),
        user=user_id if user_id else random.string(5, 25),
        service=service_name,
        attachments=[random_attachment(random) for i in attachments_amount],
        file=random_file(random),
        published=published_date,
        edited=edited_date,
        title=title,
        content=content
    )
    return post


def random_user(random: Extended_Random = dev_random) -> User:
    user = User(
        id=random.string(5, 25),
        name=random.text(3, 50),
        service=service_name,
    )

    return user


def random_dm(import_id: str, contributor_id: str, user_id: str = None, random: Extended_Random = dev_random) -> DM:
    dm = DM(
        import_id=import_id,
        id=random.string(5, 25),
        contributor_id=contributor_id,
        user=user_id if user_id else random.string(5, 25),
        service=service_name,
        file=random_file(random),
        published=random.date(),
        content=random.lorem_ipsum()
    )

    return dm


def random_file(user: str, post: str, random: Extended_Random = dev_random) -> File:
    file_path = random.choice(asset_files)
    file = File(
        name=file_path.name,
        path=file_path,
        user=user,
        post=post
    )

    return file


def random_attachment(random: Extended_Random = dev_random) -> Attachment:
    file = random_file(random)
    attachment = Attachment(
        name=file['name'],
        path=file['path'],
    )

    return attachment
