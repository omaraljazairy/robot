from flask_restful import Resource, abort
import RPi.GPIO as gpio
import time
from resources import logging, board

SLEEP_TIME = 1
logger = logging.getLogger('leds')
pin = {'front': 36,'back':21}


class Led(Resource):

    def __init__(self):

        logger.debug("led init")
        gpio.setmode(gpio.BOARD)
        setup()
        self.options = ['on','off']


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
        gpio.output(pin['back'], True)
        gpio.output(pin['fron'], True)
        return {'lights on':True}

    def off(self):
        logger.info("light off")
        gpio.output(pin['back'], False)
        gpio.output(pin['front'], False)
        return {'lights off':True}

    def front(self,on=bool):
        logger.info("light off")
        gpio.output(pin['front'], on)
        return {'front light 36':on}

    def back(self, on=bool):
        logger.info("light on: %s", on)
        gpio.output(pin['back'], on)
        return {'back light 21': on}


    def reverse(self):
        logger.info("light off")
        gpio.output(37, False)
        return {'led 37':'off'}



def setup():
    logger.info("setup executed")
    ''' setting up the leds and registering them with gpio '''
    gpio.setup(pin['back'], gpio.OUT)  # back lights
    gpio.setup(pin['front'], gpio.OUT)  # front lights
    ''' disabling the motors which will prevent the leds from turning at the start of the application '''
    gpio.output(pin['back'], False)
    gpio.output(pin['front'], False)

setup()
