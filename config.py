import logging
import sys
from flask import Flask
from flask_cors import CORS
import os
from dotenv import load_dotenv


load_dotenv()

# Configure basic logging settings
logging.basicConfig(
    stream=sys.stdout,
    format='%(asctime)s - %(name)s - %(levelname)s [%(filename)s:%(lineno)s - %(funcName)s ] - %(message)s',
    level=logging.DEBUG
)


app = Flask(__name__)

CORS(app, resources={
    r"/*": {
        "origins": os.getenv('CORS_ORIGINS'),
        "methods": ["GET", "HEAD", "POST", "OPTIONS", "PUT", "DELETE"],
        "max_age": 30
    }})
app.config['CORS_HEADERS'] = 'Content-Type'

app.config["REDIS_URL"] = os.getenv('REDIS_URL')

