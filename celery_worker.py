from celery import Celery
from tasks import create_app
from tasks.tasks import create_contact, delete_contacts


def create_celery(app):
    celery = Celery(app.import_name,
                    backend=app.config['CELERY_RESULT_BACKEND'],
                    broker=app.config['BROKER_URL'])
    celery.conf.update(app.config)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery


flask_app = create_app()
celery = create_celery(flask_app)


@celery.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    """
    Periodic task scheduler, the tasks referenced here will run at the given frequency.
    :param obj sender: Sender instance to append new periodic tasks.
    :param hash kwargs: Optional kwargs. Not used in our case.
    :return:
    """

    # The task to create random contacts: every 15 seconds
    sender.add_periodic_task(15.0, create_contact, name='Create every 15s')

    # The task to remove random contacts: every 60 seconds
    sender.add_periodic_task(60.0, delete_contacts, name='Delete every 60s')


