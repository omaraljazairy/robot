from flask import Flask
from flask_restful import Resource, Api
from resources.direction import Direction
from resources.led import Led
from config import app_config
import logging
import logging.config

app = Flask(__name__)
api = Api(app, prefix='/api/v1')
#app.config.from_pyfile('config.py')
print(app_config['testing'].DEBUG)

#file_handler = logging.FileHandler('logs/api.log')
#app.logger.addHandler(file_handler)
#app.logger.setLevel(logging.DEBUG)
logging.config.dictConfig(app_config['development'].LOGGING)
logger = logging.getLogger('directions')

logger.debug("new logging")

class Movement(Resource):

    def get(self):
        return {'direction':'bla'}

app.logger.info("first logger")
api.add_resource(Movement,'/movement/')
api.add_resource(Direction,'/directions/<string:direction>/')
api.add_resource(Led,'/leds/<string:option>/')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8009, debug=True)
