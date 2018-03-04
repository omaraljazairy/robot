from flask_restful import Resource, abort
import RPi.GPIO as gpio
import time
import os
from resources import logging, board
from resources.led import Led


SLEEP_TIME = 1 #set the sleep time of the script so the motors will not keep running

logger = logging.getLogger('directions')

def setup():
    logger.info("setup executed")
#    gpio.setwarnings(False)  # disable the warnings because they are too much
#    gpio.setmode(gpio.BOARD)  # using the board numbering on the raspberry pi
    ''' setting up the mototrs and registering them with gpio '''
    gpio.setup(7, gpio.OUT)  # motor LA
    gpio.setup(11, gpio.OUT)  # motor LB
    gpio.setup(13, gpio.OUT)  # motor RA
    gpio.setup(15, gpio.OUT)  # motor RB
    ''' disabling the motors which will prevent the mototrs from turning at the start of the application '''
    gpio.output(7, False)
    gpio.output(11, False)
    gpio.output(13, False)
    gpio.output(15, False)

setup()

class Direction(Resource):

    def __init__(self):

        self.directions = ['left','right','forward','backward','pivotright','pivotleft','stop','start','break1']
        logger.debug("direction init")
        gpio.setmode(gpio.BOARD)
        setup()
        self.led = Led()



    def get(self,direction):

        dir = str(direction).lower()
        logger.debug("dir received : %s", dir)

        error_msg = "direction " + dir + " doesn't exist"
        if dir not in self.directions:
            logger.error("%s", error_msg)
            abort(400,error=error_msg)
        else:
            getattr(self,dir)()
            return {'direction':dir}


    def start(self):
        logger.debug("car engine started")
        self.led.back(on=True)
        self.led.front(on=True)

    def stop(self):
        logger.debug("car engine stopped")
        self.led.back(on=False)
        self.led.front(on=False)

    def break1(self):

        logger.debug("break")
        self.stop()
        gpio.output(7, False)
        gpio.output(11, False)
        gpio.output(13, False)
        gpio.output(15, False)
        gpio.cleanup()

    def left(self):

        logger.debug("left")

#        self.led.back(on=True)
        self.led.front(on=True)

        gpio.output(7, False)
        gpio.output(11, False)
        gpio.output(13, True)
        gpio.output(15, False)
        gpio.cleanup()



    def right(self):

        logger.debug("right")

        self.led.back(on=True)
        self.led.front(on=True)

        gpio.output(7, False)
        gpio.output(11, True)
        gpio.output(13, False)
        gpio.output(15, False)
 #       time.sleep(SLEEP_TIME)
        gpio.cleanup()



    def forward(self):

        logger.debug("forward")

        self.led.back(on=True)
        self.led.front(on=True)

        gpio.output(7, False)
        gpio.output(11, True)
        gpio.output(13, True)
        gpio.output(15, False)
#        time.sleep(SLEEP_TIME)
        gpio.cleanup()


    def backward(self):

        logger.debug("backward")
        self.led.back(on=True)
        self.led.front(on=True)

        gpio.output(7, True)
        gpio.output(11, False)
        gpio.output(13, False)
        gpio.output(15, True)
#        time.sleep(SLEEP_TIME)
        gpio.cleanup()



    def pivotleft(self):

        logger.debug("pivotleft")

        self.led.back(on=True)
        self.led.front(on=True)

        gpio.output(7, True)
        gpio.output(11, False)
        gpio.output(13, True)
        gpio.output(15, False)
#        time.sleep(SLEEP_TIME)
        gpio.cleanup()


    def pivotright(self):

        logger.debug("pivotright")

        self.led.back(on=True)
        self.led.front(on=True)

        gpio.output(7, False)
        gpio.output(11, True)
        gpio.output(13, False)
        gpio.output(15, True)
#        time.sleep(SLEEP_TIME)
        gpio.cleanup()


#setup()