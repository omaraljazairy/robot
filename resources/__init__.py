from config import app_config
import logging.config
import RPi.GPIO as gpio

logging.config.dictConfig(app_config['development'].LOGGING)

board = gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)
