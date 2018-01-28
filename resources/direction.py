from flask_restful import Resource, abort
import RPi.GPIO as gpio
import time
import os
from resources import logging

SLEEP_TIME = 1

logger = logging.getLogger('directions')

class Direction(Resource):

    def __init__(self):

        self.directions = ['left','right','forward','backward','pivotright','pivotleft']
        logger.debug("direction init")


    def get(self,direction):

        dir = str(direction).lower()
        logger.debug("dir received : %s", dir)

        error_msg = "direction " + dir + " doesn't exist"
        if dir not in self.directions:
            logger.error("%s", error_msg)
            abort(400,error=error_msg)
        else:
            self.setup()
            getattr(self,dir)()
            return {'direction':dir}

    def setup(self):

        logger.debug("setup")

        gpio.setmode(gpio.BOARD)
        gpio.setup(7, gpio.OUT)
        gpio.setup(11, gpio.OUT)
        gpio.setup(13, gpio.OUT)
        gpio.setup(15, gpio.OUT)


    def left(self):

        logger.debug("left")

        gpio.output(7, False)
        gpio.output(11, False)
        gpio.output(13, True)
        gpio.output(15, False)
        time.sleep(SLEEP_TIME)
        gpio.cleanup()



    def right(self):

        logger.debug("right")

        gpio.output(7, False)
        gpio.output(11, True)
        gpio.output(13, False)
        gpio.output(15, False)
        time.sleep(SLEEP_TIME)
        gpio.cleanup()



    def forward(self):

        logger.debug("forward")

        gpio.output(7, False)
        gpio.output(11, True)
        gpio.output(13, True)
        gpio.output(15, False)
        time.sleep(SLEEP_TIME)
        gpio.cleanup()


    def backward(self):

        logger.debug("backward")

        gpio.output(7, True)
        gpio.output(11, False)
        gpio.output(13, False)
        gpio.output(15, True)
        time.sleep(SLEEP_TIME)
        gpio.cleanup()



    def pivotleft(self):

        logger.debug("pivotleft")

        gpio.output(7, True)
        gpio.output(11, False)
        gpio.output(13, True)
        gpio.output(15, False)
        time.sleep(SLEEP_TIME)
        gpio.cleanup()


    def pivotright(self):

        logger.debug("pivotright")


        gpio.output(7, False)
        gpio.output(11, True)
        gpio.output(13, False)
        gpio.output(15, True)
        time.sleep(SLEEP_TIME)
        gpio.cleanup()

