#Created by Eric McAfee

import psycopg2
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World from Eric McAfee in 3308!'

@app.route('/db_test')
def db_test():
    conn = conn = psycopg2.connect("postgresql://render_tutorial_db_user:cQINwvX4yWTeP2NinFsZ2NIEA536CX6f@dpg-cvhkpkhc1ekc738cjee0-a/render_tutorial_db")
    conn.close()
    return "Database Connection Successful"
