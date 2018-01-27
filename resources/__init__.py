from config import app_config
import logging.config

logging.config.dictConfig(app_config['development'].LOGGING)