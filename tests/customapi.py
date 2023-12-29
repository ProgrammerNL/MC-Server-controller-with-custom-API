import json
from flask import *
import time

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home_page():
    data_set = {'Page': 'Home' 'Message': 'Succesfully loaded the home page', 'Timestamp': time.time()}
    json_dump = json.dumps(data_set)
    
    return json_dump