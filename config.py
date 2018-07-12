

class Config(object):
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CELERY_TIMEZONE = 'Europe/Dublin'
    BROKER_URL = 'redis://guest@localhost:6379/'
    CELERY_RESULT_BACKEND = 'redis://guest@localhost:6379/'
    CELERY_SEND_TASK_SENT_EVENT = True
    CONTACT_API_URL = 'http://0.0.0.0:7000/'


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    pass


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
