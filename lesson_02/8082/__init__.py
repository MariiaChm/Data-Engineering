from flask import Flask, request, abort
import os
import json
import fastavro
import sys
import schemas

sys.path.append('../')
from common_methods import create_or_clear_directory

app = Flask(__name__)

AUTH_TOKEN = os.environ['AUTH_TOKEN']
