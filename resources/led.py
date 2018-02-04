from flask_restful import Resource, abort
import RPi.GPIO as gpio
import time
from gpiozero import LED
from resources import logging

SLEEP_TIME = 1
logger = logging.getLogger('leds')

class Led(Resource):

    def __init__(self):

        self.options = ['on','off','blink']
        logger.debug("led init")
        setup_modes()

    def get(self, option):
        if str(option).lower() not in (self.options):
            error_msg = "option " + str(option) + " is not supported"
            logger.error(error_msg)
            abort(400, error=error_msg)
        else:
            logger.info("option chosen :%s ", option)
            return getattr(self, option)()

    def on(self):
        logger.info("light on")
        gpio.output(37, True)
        return {'led 37':'on'}

    def off(self):
        logger.info("light off")
        gpio.output(37, False)
        self.blink()
        return {'led 37':'off'}

    def blink(self):
        logger.info("blink on")
        amber = LED(26)
        # amber.on()
        amber.blink(0.5, 0.5, 5, False)  # blink(on,off,times to blink,keep on)
        return {'led 26':'blink'}

def setup_modes():
    logger.debug("setup modes")
    gpio.setmode(gpio.BOARD)
    gpio.setwarnings(False)
    gpio.setup(37, gpio.OUT)
