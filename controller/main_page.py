from flask import Flask, render_template, request, redirect, url_for
from app_init import app
from training.result import predict
from datetime import datetime
from connect_db import connect_db

@app.route('/')
def goToMainPage():
    return redirect(url_for('showMainPage'))

@app.route('/main-page')
def showMainPage():
    return render_template('main-page.html')

@app.route('/main-page', methods=['POST'])
def post():
    _content = request.form['comment_text']
    label = str(predict(_content))
    label = label.removeprefix('__label__')
    label = label.replace('_', ' ')
    now = datetime.now()
    username = 'test1'
    connect_db.cursor().execute('insert into posts (username, content, postAt, label) values (?, ?, ?, ?)', (username, _content, now, label))
    connect_db.commit()
    return redirect(url_for('showMainPage'))