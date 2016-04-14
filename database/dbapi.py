import pymysql.cursors
import pymysql.err
import os
import json


def connect():
    try:
        # Specify config in database.json or editing 'database' variable below
        db_config_file = os.path.join(os.path.dirname(__file__), "database.json")

        if os.path.exists(db_config_file):
            with open(db_config_file) as f:
                database = json.load(f)
        else:
                database = [ {"host":"localhost", "db":"test", "user":"root", "passwd":""}]

        connection = pymysql.connect(host=database[0]['host'],
                                     user=database[0]['user'],
                                     passwd=database[0]['passwd'],
                                     db=database[0]['db'],
                                     charset='utf8',
                                     cursorclass=pymysql.cursors.DictCursor)
        return connection
    except pymysql.err.Error as e:
        print('An error occurred. Error {!r}, errno is {}'.format(e, e.args[0]))
        raise # let the exception raise to the caller

def get_categories():
    try:
        connection = connect()  # return db connection

        c = connection.cursor()

        # Populate for category drop-down
        c.execute("SELECT * FROM categories ORDER BY category_id") 
        categories = c.fetchall()
    finally:
        c.close() # make sure the connection gets closed

    return categories
