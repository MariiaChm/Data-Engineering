from flask import Flask, request, abort
import os
import json
import sys
import requests

sys.path.append('../')
from common_methods import create_or_clear_directory

app = Flask(__name__)

AUTH_TOKEN = os.environ['AUTH_TOKEN']

URL = 'https://fake-api-vycpfa6oca-uc.a.run.app/sales'
