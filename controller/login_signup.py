from flask import Flask, render_template, request, redirect, url_for
from app_init import app
from connect_db import connect_db
import pandas as pd
import re

@app.route('/')
def hello():
    return redirect(url_for('login'))

@app.route('/login')
def showLogin():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    users = connect_db.cursor().execute('select * from users')
    _username = request.form['fname']
    _password = request.form['fpass']
    for user in users:
        if _username == user[0] and _password == user[1]:
            return "Welcoms"
        if _username == user[0]:
            return render_template('login.html', passError = 1, username = _username)
    return render_template('login.html', usernameError = 1, username = _username)

@app.route('/signup')
def showSignup():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def signup():
    _username = request.form['fname']
    _password = request.form['fpass']
    _repass = request.form['fRepass']
    _fullname = request.form['fFullname']
    _phone = request.form['fphone']
    _email = request.form['fEmail']
    checkUsername = connect_db.cursor().execute('select * from users where username = ?', _username).fetchall()
    checkPhone = connect_db.cursor().execute('select * from users where username = ?', _phone).fetchall()
    checkEmail = connect_db.cursor().execute('select * from users where username = ?', _email).fetchall()
    if len(checkUsername) != 0:
        return render_template('signup.html', usernameError = 1, username = _username, fullname = _fullname, phone = _phone, email = _email)
    if _password != _repass:
        return render_template('signup.html', passwordError = 1, username = _username, fullname = _fullname, phone = _phone, email = _email)
    # if len(_phone) != 10:
    #     return render_template('signup.html', phoneError = 1, username = _username, fullname = _fullname, phone = _phone, email = _email)
    if len(checkPhone) != 0:
        return render_template('signup.html', phoneRepeat = 1, username = _username, fullname = _fullname, phone = _phone, email = _email)
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if not re.fullmatch(regex, _email):
        return render_template('signup.html', emailError = 1, username = _username, fullname = _fullname, phone = _phone, email = _email)
    if len(checkEmail) != 0:
        return render_template('signup.html', emailRepeat = 1, username = _username, fullname = _fullname, phone = _phone, email = _email)
    connect_db.cursor().execute('insert into users values (?, ?, ? ,?, ?)', (_username, _password, _fullname, _email, _phone))
    connect_db.commit()
    return redirect(url_for('login'))




