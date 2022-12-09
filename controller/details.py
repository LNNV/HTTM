from flask import Flask, render_template, request, redirect, url_for
from app_init import app
from datetime import datetime
from connect_db import connect_db

@app.route('/details')
def showDetails():
    user = request.cookies.get('user')
    label = request.args.get('label', '')
    if label == '': 
        return redirect(url_for('showMainPage'))
    posts = connect_db.cursor().execute('select * from posts where label=?', label).fetchall()
    return render_template('details.html', able_search = 1, user=user, label=label, posts=posts)

@app.route('/details/search', methods=['POST'])
def search():
    user = request.cookies.get('user')
    label = request.args.get('label', '')
    _search = request.form['search']
    _search = "%" + _search + "%"
    print(_search)
    if label == '':
        posts = connect_db.cursor().execute('select * from posts where username LIKE ? OR content LIKE ?', (_search, _search)).fetchall()
    else:
        posts = connect_db.cursor().execute('select * from posts where label=? AND (username LIKE ? OR content LIKE ?)', (label, _search, _search)).fetchall()
    return render_template('details.html', user=user, posts=posts)