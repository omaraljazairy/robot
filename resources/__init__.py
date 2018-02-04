from config import app_config
import logging.config
import RPi.GPIO as gpio

logging.config.dictConfig(app_config['development'].LOGGING)

gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)
