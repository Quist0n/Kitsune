import sys

from development.internals import dev_random
from .randoms import random_post, random_user, random_dm
from .users import import_users
from .dms import import_dms
from .posts import import_posts, get_files_from_posts
from .files import import_files

from development.types import Extended_Random
sys.setrecursionlimit(100000)


def run_paysite_import(import_id: str, key: str, contributor_id: str, random: Extended_Random = dev_random):
    """Runs the importer."""

    user_amount = range(random.randint(3, 15))
    users = [random_user() for index in user_amount]

    post_users = random.sample(users, random.randint(1, len(users)))
    dm_users = random.sample(users, random.randint(1, len(users)))

    post_amount = range(random.randint(23, 117))
    posts = [random_post(random=random) for index in post_amount]
    posts.extend([random_post(user['id'], random) for user in post_users])

    dm_amount = range(random.randint(7, 13))
    dms = [random_dm(import_id, contributor_id, random=random) for index in dm_amount]
    dms.extend([random_dm(import_id, contributor_id, user['id'], random) for user in dm_users])

    files = get_files_from_posts(posts)

    import_dms(import_id, dms)
    import_users(import_id, users)
    import_posts(import_id, posts)
    import_files(files)
