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

@app.route('/db_create') #Creates the basketball table in the PostgrSQL db and returns a string to the browser to confirm.
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

@app.route('/db_insert') #Populates the basketball table and returns a string to the browser to confirm.
def db_insert():
    conn = conn = psycopg2.connect("postgresql://render_tutorial_db_user:cQINwvX4yWTeP2NinFsZ2NIEA536CX6f@dpg-cvhkpkhc1ekc738cjee0-a/render_tutorial_db")
    cur = conn.cursor()
    cur.execute('''
    INSERT INTO Basketball (First, Last, City, Name, Number)
    Values
    ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
    ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
    ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
    ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
    ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Populated"

@app.route('/db_select') # Queries the basketball table, then loops over the response and formats it into a string with html tags before returning to the browser
def db_select():
    conn = conn = psycopg2.connect("postgresql://render_tutorial_db_user:cQINwvX4yWTeP2NinFsZ2NIEA536CX6f@dpg-cvhkpkhc1ekc738cjee0-a/render_tutorial_db")
    cur = conn.cursor()
    cur.execute('''
        SELECT * FROM Basketball;
    ''')
    records = cur.fetchall()
    conn.close()
    response_string = ""
    response_string += "<table>"
    for player in records:
        response_string += "<tr>"
        for info in player:
            response_string += "<td>{}</td>".format(info)
        response_string +="</tr>"
    response_string += "</table>"
    return response_string

@app.route('/db_drop') #drops the basketball table from the PostgreSQL db
def deb_drop():
    conn = conn = psycopg2.connect("postgresql://render_tutorial_db_user:cQINwvX4yWTeP2NinFsZ2NIEA536CX6f@dpg-cvhkpkhc1ekc738cjee0-a/render_tutorial_db")
    cur = conn.cursor()
    cur.execute('''
    DROP TABLE Basketball;
    ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Dropped"

