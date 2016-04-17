from bottle import route, view, template, request, response, redirect
import pymysql.cursors
import pymysql.err
import os
import json
from database import dbapi


@route('/generate_reports', method=['GET'])
@view('generate_reports')
def view_generate_reports():
    return {'message':''}

@route('/generate_reports', method=['POST'])
@view('generate_reports')
def report_select():

    report_type = request.forms.get('report_type', '').strip()

    if report_type == "inventory":
        redirect('/inventory_report')
    elif report_type == "clerk":
        redirect('/clerk_report')
    else:
        redirect('/customer_report')