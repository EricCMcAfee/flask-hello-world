#Created by Eric McAfee
#March 25th, 2025

import psycopg2
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World from Eric McAfee in 3308!'

@app.route('/db_test') #establishes connection to our PostgreSQL db and returns a string to the browser to confirm.
def db_test():
    conn = conn = psycopg2.connect("postgresql://render_tutorial_db_user:cQINwvX4yWTeP2NinFsZ2NIEA536CX6f@dpg-cvhkpkhc1ekc738cjee0-a/render_tutorial_db")
    conn.close()
    return "Database Connection Successful"

@app.route('/db_create') #Creates a table in the PostgrSQL db and returns a string to the browser to confirm.
def db_create():
    conn = conn = psycopg2.connect("postgresql://render_tutorial_db_user:cQINwvX4yWTeP2NinFsZ2NIEA536CX6f@dpg-cvhkpkhc1ekc738cjee0-a/render_tutorial_db")
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Basketball(
        First varchar(255),
        Last varchar(255),
        City varchar(255),
        Name varchar(255),
        Number int
        );
''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Created"
