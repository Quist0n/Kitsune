from flask import Blueprint, request
from datetime import datetime

from development.internals import dev_random, dev_seed, dev_max_date
from development.lib import importer, randoms
from development.lib.service_key import get_service_keys, kill_service_keys
from development.types import Extended_Random
from src.internals.utils import logger
from src.internals.utils.utils import get_import_id
from src.internals.utils.flask_thread import FlaskThread
from src.lib import import_manager
from src.lib.autoimport import encrypt_and_save_session_for_auto_import

development = Blueprint('development', __name__)


@development.route('/development', methods=['GET'])
def health_check():
    return '', 200


@development.route('/development/test-entries/seeded', methods=['POST'])
def generate_seeded_entries():
    test_random = Extended_Random(dev_seed, dev_max_date)
    key = dev_random.string(127, 255)
    import_id = get_import_id(key)
    # service = service_name
    target = importer.import_posts
    contributor_id: str = request.form.get("account_id")
    args = (key, contributor_id, test_random)

    if target and args:
        logger.log(
            import_id, f'Starting import. Your import id is \"{import_id}\".')
        FlaskThread(
            target=import_manager.import_posts,
            args=(import_id, target, args)
        ).start()
    else:
        logger.log(
            import_id, f'Error starting import. Your import id is \"{import_id}\".'
        )

    return import_id, 200


@development.route('/development/test-entries/random', methods=['POST'])
def generate_random_entries():
    key = dev_random.string(127, 255)
    import_id = get_import_id(key)
    # service = service_name
    target = importer.import_posts
    contributor_id: str = request.form.get("account_id")
    args = (key, contributor_id)

    if target and args:
        logger.log(import_id, f'Starting import. Your import id is \"{import_id}\".')
        FlaskThread(
            target=import_manager.import_posts,
            args=(import_id, target, args)
        ).start()
    else:
        logger.log(import_id, f'Error starting import. Your import id is \"{import_id}\".')

    return import_id, 200


@development.route('/development/service-keys', methods=['POST'])
def generate_service_keys():
    """
    TODO: fix it to work with the new keys system.
    """
    account_id: str = request.form.get('account_id')

    service_keys = [randoms.service_key(account_id)
                    for key in range(dev_random.randint(15, 35))]

    for service_key in service_keys:
        encrypt_and_save_session_for_auto_import(
            service=service_key['service'],
            key=service_key['key'],
            contributor_id=service_key['contributor_id']
        )
        print(
            f"Saved {service_keys.index(service_key) + 1} keys out of {len(service_keys)}.")

    targets_amount = dev_random.randint(1, len(service_keys) - 1)
    marked_keys = get_service_keys(targets_amount)
    print(marked_keys)
    print(f"{len(marked_keys)} keys are marked for kill.")
    kill_service_keys(marked_keys)
    return '', 200
