from bottle import route, view, request, response
from datetime import datetime
import pymysql.cursors

import os
import json

# Specify config in database.json or editing 'database' variable below
db_config_file = os.path.join(os.path.dirname(__file__), "database.json")
print(db_config_file)

if os.path.exists(db_config_file):
    with open(db_config_file) as f:
        database = json.load(f)
else:
        database = [ {"host":"localhost", "db":"test", "user":"root", "passwd":""}]

# Establish Databse Connection
#connection = []
#for param in database:
#    connection.append(pymysql.connect(**param))

connection = pymysql.connect(host=database[0]['host'],
                             user=database[0]['user'],
                             passwd=database[0]['passwd'],
                             db=database[0]['db'],
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)


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
