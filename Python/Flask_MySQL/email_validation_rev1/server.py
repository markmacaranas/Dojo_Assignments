from flask import Flask, render_template, redirect, request, flash
from mysqlconnection import MySQLConnector
import re
app = Flask(__name__)
app.secret_key = "dlkjfoaiduf98aeu"
mysql = MySQLConnector(app, 'email_validation')

@app.route('/')
def index():
    allemails = mysql.query_db  ("SELECT * FROM emails")
    print "got all the emails", allemails
    return render_template('index.html')

@app.route('/process', methods=["post"])
def process():
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    if len(request.form['email']) < 1:
        flash('Email cannot be blank!')
        return redirect ('/')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash('Invalid Email Address!')
        return redirect ('/')
    else:
        flash('Success!')
        query = 'INSERT INTO emails (email, created_at, updated_at) VALUES (:email, NOW(), NOW())'
        data = {'email': request.form['email']}
        newuserid = mysql.query_db(query, data)

    return redirect('/success')

@app.route('/success')
def success():
    allemails = mysql.query_db("SELECT * FROM emails")
    print "all the emails", allemails
    return render_template('success.html', emails = allemails)


app.run(debug=True)
