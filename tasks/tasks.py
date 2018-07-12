import json
import requests

from tasks.services import set_contact_payload
from celery.utils.log import get_task_logger
from tasks import celery

logger = get_task_logger(__name__)


@celery.task
def create_contact(create_url):
    """
    Task creating a random contact by calling the contact API.
    :param create_url: The URL to call to add a contact.
    e.g: http://0.0.0.0:7000/contacts
    :return:
    """

    contact_payload = set_contact_payload()

    logger.info('-- Sending payload {} to contact API for contact creation. -- '.format(contact_payload))
    result = requests.post(create_url, data=json.dumps(contact_payload))
    logger.info('-- Response from contact API is {} --'.format(result.json()))


@celery.task
def delete_contacts(delete_url):
    """
    Task deleting contacts by calling the contact API.
    :param delete_url: The URL to call to add a contact.
    e.g: http://0.0.0.0:7000/contacts/60 to delete all the entries inserted before 60 seconds from now.
    :return:
    """
    logger.info('-- Deleting contacts created 1 minute from now --')
    result = requests.delete(delete_url)
    logger.info('-- Status code from delete contacts API is {} --'.format(result.status_code))
