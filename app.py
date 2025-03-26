#Created by Eric McAfee

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World from Eric McAfee in 3308!'
