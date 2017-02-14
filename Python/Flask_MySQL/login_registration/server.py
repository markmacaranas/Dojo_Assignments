from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = 'loginregistration'
mysql = MySQLConnector(app, 'login_reg')

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
