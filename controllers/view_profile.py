from bottle import route, view, template, request, response
import pymysql.cursors
import pymysql.err
import os
import json


@route('/view_profile/<cust_id>')
@view('view_profile')
def view_profile(cust_id):

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

        c = connection.cursor()

        sql = "SELECT * FROM customers WHERE customer_id = %s"

        c.execute(sql,cust_id)
        data = c.fetchone()
        c.close()
    except pymysql.err.Error as e:
        return template('login.tpl', message='An error occurred. Error {!r}, errno is {}'.format(e, e.args[0]))
    else:
        data['message']=''  # Template expects a message.  Used for debugging or informing the user of something without altering the template
        return data
