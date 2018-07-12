from celery import Celery
from tasks import create_app
from tasks.tasks import create_contact, delete_contacts


def create_celery(flask_application):
    """
    Creating the Celery application instance.
    :param obj flask_application: The Flask application instance.
    :return:
    """
    celery_app = Celery(flask_application.import_name,
                        backend=flask_application.config['CELERY_RESULT_BACKEND'],
                        broker=flask_application.config['BROKER_URL'])
    celery_app.conf.update(flask_application.config)
    celery_task = celery_app.Task

    class ContextTask(celery_task):
        abstract = True

        def __call__(self, *args, **kwargs):
            with flask_application.app_context():
                return celery_task.__call__(self, *args, **kwargs)

    celery_app.Task = ContextTask
    return celery_app


application = create_app()
celery = create_celery(application)


@celery.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    """
    Periodic task scheduler, the tasks referenced here will run at the given frequency.
    :param obj sender: Sender instance to append new periodic tasks.
    :param hash kwargs: Optional kwargs. Not used in our case.
    :return:
    """

    # The task to create random contacts: every 15 seconds
    sender.add_periodic_task(15, create_contact,
                             args=(application.config['CONTACT_API_URL'],),
                             name='Create every 15s')

    # The task to remove random contacts: every 60 seconds
    delete_from_seconds = 60
    sender.add_periodic_task(delete_from_seconds, delete_contacts,
                             args=(application.config['CONTACT_API_URL'] + '/' + str(delete_from_seconds),),
                             name='Delete every 60s')


