import os

class Config(object):
    """Parent configuration class."""
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = os.getenv('SECRET')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    HOME_DIR = os.path.join(BASE_DIR,'robotic/')
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'standard': {
                'format': "[%(asctime)s] [%(threadName)s] [%(thread)d] [%(process)d] [%(levelname)s] [%(name)s:%(lineno)s] %(message)s",
                'datefmt': "%d/%b/%Y %H:%M:%S"
            },
        },
        'handlers': {
            'file': {
                'level': 'DEBUG',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': os.path.join(HOME_DIR, 'logs/api.log'),
                'formatter': 'standard',
            },
            'console': {
                'level': 'INFO',
                'class': 'logging.StreamHandler',
                'formatter': 'standard'
            },
        },
        'loggers': {
            'directions': {
                'handlers': ['file'],
                'level': 'DEBUG',
                'propagate': True,
            },
            'camera': {
                'handlers': ['file'],
                'level': 'DEBUG',
                'propagate': True,
            },
            'leds': {
                'handlers': ['file'],
                'level': 'DEBUG',
                'propagate': True,
            },
            'ultrasone': {
                'handlers': ['file'],
                'level': 'DEBUG',
                'propagate': True,
            },
            'tpr': {
                'handlers': ['file'],
                'level': 'DEBUG',
                'propagate': True,
            },
        },
    }
    


class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True

class TestingConfig(Config):
    """Configurations for Testing, with a separate test database."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/test_db'
    DEBUG = True

class StagingConfig(Config):
    """Configurations for Staging."""
    DEBUG = True

class ProductionConfig(Config):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False

app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}