from bottle import route, view, template, request, response, redirect
import pymysql.cursors
import pymysql.err
import os
import json


@route('/create_tool', method=['GET','POST'])
@view('create_tool')
def new_profile():

    if request.forms.get('Submit', '').strip():

        short_description = request.forms.get('short_description', '').strip()
        full_description = request.forms.get('full_description', '').strip()
        deposit = request.forms.get('deposit', '').strip()
        day_price = request.forms.get('day_price', '').strip()
        original_price = request.forms.get('original_price', '').strip()
        category_id = request.forms.get('category_id', '').strip()

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

            # Populate for category drop-down
            c.execute("SELECT * FROM categories;") 
            rows = c.fetchall()

            sql = "INSERT INTO tools(short_description, full_description, deposit, day_price, original_price, category_id) VALUES (%s, %s, %s, %s, %s, %s)"

            c.execute(sql,(short_description, full_description, deposit, day_price, original_price, category_id))
            tool_id = c.lastrowid
            connection.commit()

        except pymysql.err.IntegrityError:
            return template('create_tool.tpl', message="The tool already exists.")
        except pymysql.err.Error as e:
            return template('login.tpl', message='An error occurred. Error {!r}, errno is {}'.format(e, e.args[0]))
        else:
            c.close()
            #return template('view_profile.tpl', message='New customer profile created.', cust_id=cust_id)
            redirect("/view_tool/%s" % tool_id)
    else:
        return template('create_tool.tpl', message='')
