from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
app = Flask(__name__)
app.secret_key = 'asdlfkkja'
mysql = MySQLConnector(app, 'valid_emails')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/email', methods=['POST'])
def check():
    if not EMAIL_REGEX.match(request.form['email']):
        flash('Email is not valid!')
        return redirect('/')
    else:
        flash('The email address you entered ' + request.form['email'] + ' is a VALID email address! Thank you!')
        query = "INSERT INTO emails (email,created_at) VALUES (:email, NOW())"
        data = {
            'email': request.form['email']
            }
        mysql.query_db(query, data)
        return redirect('/success')

@app.route('/success')
def success():
    query = "SELECT * FROM emails"
    emails = mysql.query_db(query)
    return render_template('success.html', all_emails=emails)

app.run(debug=True)
