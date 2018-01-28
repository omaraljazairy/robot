from flask_restful import Resource, abort
import RPi.GPIO as GPIO
import time
import os
from resources import logging

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(37, GPIO.OUT)

SLEEP_TIME = 1
logger = logging.getLogger('leds')

class Led(Resource):

    def __init__(self):

        self.options = ['on','off']
        logger.debug("led init")

    def get(self, option):
        if str(option).lower() not in (self.options):
            error_msg = "option " + str(option) + "is not supported"
            logger.error(error_msg)
            abort(400, error=error_msg)
        else:
            logger.info("option chosen :%s ", option)
            return getattr(self, option)

    def on(self):
        logger.info("light on")
        GPIO.output(37, True)

    def off(self):
        logger.info("light off")
        GPIO.output(37, False)

