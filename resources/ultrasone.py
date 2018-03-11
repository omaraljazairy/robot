from flask_restful import Resource, abort
import RPi.GPIO as gpio
import time
from resources import logging

SLEEP_TIME = 1
GPIO_TRIGGER = 38
GPIO_ECHO = 40

#GPIO Mode (BOARD / BCM)


logger = logging.getLogger('ultrasone')

class Ultrasone(Resource):

    def __init__(self):
        # set GPIO direction (IN / OUT)
        gpio.setmode(gpio.BOARD)
        setup()
        logger.debug("ultrasone initialized")
        self.options = ['start']

    def get(self, option):
        if str(option).lower() not in (self.options):
            error_msg = "option " + str(option) + " is not supported"
            logger.error(error_msg)
            abort(400, error=error_msg)
        else:
            logger.info("option chosen :%s ", option)
            return self.start_sensor()


    def distance(self):

        logger.info("distance started")
        # set Trigger to HIGH
        gpio.output(GPIO_TRIGGER, True)

        # set Trigger after 0.01ms to LOW
        time.sleep(0.00001)
        gpio.output(GPIO_TRIGGER, False)

        StartTime = time.time()
        StopTime = time.time()

        # save StartTime
        while gpio.input(GPIO_ECHO) == 0:
            StartTime = time.time()

        # save time of arrival
        while gpio.input(GPIO_ECHO) == 1:
            StopTime = time.time()

        # time difference between start and arrival
        TimeElapsed = StopTime - StartTime
        logger.debug("StopTime: %s - StartTime: %s =  TimeElapsed: %s", str(round(StopTime,1)), str(round(StartTime,1)), str(round(TimeElapsed,1)))
        # multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because there and back
        distance = (TimeElapsed * 34300) / 2
#        logger.debug("distance = (TimeElapsed * 34300) / 2 => %s", str(distance))

        return distance

    def start_sensor(self):
        logger.info("start_sensor started")
        try:
            while True:
                dist = self.distance()
                print("Measured Distance = %.1f cm" % dist)
                logger.debug("Measured Distance = %s cm",round(dist,1))
                time.sleep(1)

        # Reset by pressing CTRL + C
        except KeyboardInterrupt:
            print("Measurement stopped by User")
            gpio.cleanup()


def setup():
    gpio.setup(GPIO_TRIGGER, gpio.OUT)
    gpio.setup(GPIO_ECHO, gpio.IN)

setup()