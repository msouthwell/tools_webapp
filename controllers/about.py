from bottle import route, view, request, response
from datetime import datetime
import pymysql.cursors

import os
import json

connection = pymysql.connect(host='localhost',
                             db='handymandb',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)

# Specify config in database.json or editing 'database' variable below
db_config_file = os.path.join(os.path.dirname(__file__), "database.json")

if os.path.exists(db_config_file):
    with open(db_config_file) as f:
        database = json.load(f)
else:
        database = [ {"host":"localhost", "db":"test", "user":"root", "passwd":""}]

# Establish Databse Connection
connection = []
for param in database:
    connection.append(pymysql.connect(**param))

cursor = connection.cursor()


@route('/about')
@view('about')
def about():
    """Renders the about page."""
    sql = "SELECT * FROM clerks"
    cursor.execute(sql)
    row = cursor.fetchone()
    connection.close()
    return dict(
        title='About',
        message=row,
        year=datetime.now().year)
