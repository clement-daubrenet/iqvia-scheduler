import json
import requests

from .services import set_contact_payload
from celery.utils.log import get_task_logger
from tasks import celery

logger = get_task_logger(__name__)


@celery.task
def create_contact():
    """
    Task creating a random contact by calling the contact API.
    :return:
    """

    contact_payload = set_contact_payload()

    logger.info('-- Sending payload {} to contact API for contact creation. -- '.format(contact_payload))
    result = requests.post('http://0.0.0.0:7000/contacts', data=json.dumps(contact_payload))
    logger.info('-- Response from contact API is {} --'.format(result.json()))


@celery.task
def delete_contacts():
    """
    Task deleting contacts created before 1 minute from now.
    :return:
    """
    logger.info('-- Deleting contacts created 1 minute from now --')
    result = requests.delete('http://0.0.0.0:7000/contacts/1')
    logger.info('-- Status code from delete contacts API is {} --'.format(result.status_code))
