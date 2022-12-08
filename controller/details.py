from flask import Flask, render_template, request, redirect, url_for
from app_init import app
from datetime import datetime
from connect_db import connect_db

@app.route('/details')
def showDetails():
    label = request.args.get('label', '')
    if label == '': 
        return redirect(url_for('showMainPage'))
    posts = connect_db.cursor().execute('select * from posts where label=?', label).fetchall()
    return render_template('details.html', posts=posts)