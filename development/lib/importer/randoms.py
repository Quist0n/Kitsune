from development.internals import service_name, dev_random
from development.types import Extended_Random

from .types import Post_Model, User

def random_post(random: Extended_Random = dev_random) -> Post_Model:
    post: Post_Model = {
        'id': random.string(5, 25),
        '"user"': random.string(5, 25),
        'service': service_name
    }
    return post


def random_user(random: Extended_Random = dev_random) -> User:
    user = User(
        id = random.string(5, 25),
        service = service_name

    )
    return user
