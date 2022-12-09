from flask import Flask, render_template, request, redirect, url_for, make_response
from app_init import app
from training.result import predict
from datetime import datetime
from connect_db import connect_db

@app.route('/')
def goToMainPage():
    return redirect(url_for('showMainPage'))

@app.route('/main-page')
def showMainPage():
    posts = connect_db.cursor().execute('select * from posts').fetchall()
    posts = list(reversed(posts))
    user = request.cookies.get('user')
    feedback = connect_db.cursor().execute('select * from feedback').fetchall()
    feedback = list(reversed(feedback))
    label_dict1 = {
        'công nghệ': 0,
        'du lịch': 0,
        'giáo dục': 0,
        'giải trí': 0,
        'kinh doanh': 0,
        'nhịp sống': 0,
    }
    label_dict2 = {
        'phim ảnh': 0,
        'pháp luật': 0,
        'sống trẻ': 0,
        'sức khỏe': 0,
        'thế giới': 0,
        'thể thao': 0,
    }
    label_dict3 = {
        'thời sự': 0,
        'thời trang': 0,
        'xe 360': 0,
        'xuất bản': 0,
        'âm nhạc': 0,
        'ẩm thực': 0,
    }
    for p in posts:
        if p[4] in label_dict1.keys(): label_dict1[p[4]] += 1
        if p[4] in label_dict2.keys(): label_dict2[p[4]] += 1
        if p[4] in label_dict3.keys(): label_dict3[p[4]] += 1
    return render_template('main-page.html', user=user, posts=posts, feedback=feedback,
                           label_dict1=label_dict1, label_dict2=label_dict2, label_dict3=label_dict3)


@app.route('/main-page', methods=['POST'])
def post():
    user = request.cookies.get('user')
    if user == None: return redirect('/login')
    _content = request.form['comment_text']
    label = str(predict(_content))
    label = label.removeprefix('__label__')
    label = label.replace('_', ' ')
    now = datetime.now()
    connect_db.cursor().execute('insert into posts (username, content, postAt, label) values (?, ?, ?, ?)', (user, _content, now, label))
    connect_db.commit()
    return redirect(url_for('showMainPage'))

@app.route('/logout')
def logout():
    resp = make_response(redirect('/main-page'))
    resp.set_cookie('user', expires=0)
    return resp

@app.route('/send-feedback', methods=['POST'])
def send_feedback():
    user = request.cookies.get('user')
    if user == None: return redirect('/login')
    _content =request.form['feedback']
    now = datetime.now()
    connect_db.cursor().execute('insert into feedback (username, content, postAt) values (?, ?, ?)', (user, _content, now))
    connect_db.commit()
    return redirect(url_for('showMainPage'))
