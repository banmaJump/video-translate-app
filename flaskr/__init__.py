from flask import Flask

app = Flask(__name__)

from . import index
from . import process_video