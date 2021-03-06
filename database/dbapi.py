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

        c.execute("SELECT * FROM categories ORDER BY category_id")
        categories = c.fetchall()
    finally:
        c.close() # make sure the connection gets closed

    return categories

def get_available_tools(category, start_date_datetime, end_date_datetime):
    try:
        connection = connect()  # return db connection

        c = connection.cursor()

        c.execute("SELECT t.tool_id, t.short_description, t.deposit, t.day_price FROM tools AS t " +
                  "WHERE category_id = %s " +
                  "AND NOT EXISTS(SELECT * FROM reservations AS r JOIN reservations_tools AS rt ON r.reservation_id = rt.reservation_id WHERE t.tool_id = rt.tool_id AND r.start_date <= %s AND r.end_date >= %s) " +
                  "AND NOT EXISTS(SELECT * FROM service_orders AS so WHERE t.tool_id = so.tool_id AND so.start_date <= %s AND so.end_date >= %s) " +
                  "AND NOT EXISTS(SELECT * FROM sells AS s WHERE t.tool_id = s.tool_id)", (category, end_date_datetime, start_date_datetime, end_date_datetime, start_date_datetime))
        print('get_available_tools: ' + str(c._last_executed))

        tools = c.fetchall()
    finally:
        c.close()

    return tools

def check_available_tools(reserved_tools, start_date_datetime, end_date_datetime):
    try:
        connection = connect()  # return db connection

        c = connection.cursor()

        c.execute("SELECT t.tool_id, t.short_description, t.deposit, t.day_price FROM tools AS t " +
                  "WHERE NOT EXISTS(SELECT * FROM reservations AS r JOIN reservations_tools AS rt ON r.reservation_id = rt.reservation_id WHERE t.tool_id = rt.tool_id AND r.start_date <= %s AND r.end_date >= %s) " +
                  "AND NOT EXISTS(SELECT * FROM service_orders AS so WHERE t.tool_id = so.tool_id AND so.start_date <= %s AND so.end_date >= %s) " +
                  "AND NOT EXISTS(SELECT * FROM sells AS s WHERE t.tool_id = s.tool_id)", (end_date_datetime, start_date_datetime, end_date_datetime, start_date_datetime))
        print('check_available_tools: ' + str(c._last_executed))

        tools = c.fetchall()

        # return any tools not in the result set
        no_longer_available = []

        # should be able to do this in the query, but python is getting the better of me
        for reserved_tool in reserved_tools:
            found = False
            for tool in tools:
                if tool['tool_id'] == reserved_tool['tool_id']:
                    found = True
                    break
            if not found:
                no_longer_available.append(reserved_tool)
    finally:
        c.close()

    return no_longer_available
