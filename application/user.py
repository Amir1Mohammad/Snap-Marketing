#!/usr/bin/env python
# -*- coding: utf-8 -*-
# find . -name "*.pyc" -exec rm -rf {} \;

# Python import:
from flask import render_template

__Author__ = "Amir Mohammad"

# Project import :
from application import app
from models.user import User
from application.extension import db
from garbage import create_id_user


# simple input http://0.0.0.0:8000/su/'amir@iust.com'/123456/amir/mohammadi/Male/1374/09121234567
@app.route('/su/<email>/<passwordhash>/<firstname>/<lastname>/<gender>/<birth_date>/<phones>',
           methods=['GET', 'POST'])
def signup(email, passwordhash, firstname, lastname, gender, birth_date, phones):
    g = User(id=create_id_user(), email=email, passwordhash=passwordhash, firstname=firstname, lastname=lastname,
             gender=gender, birth_date=birth_date, phones=phones)
    db.session.add(g)
    db.session.commit()
    return '''
    <h2>User added Completely ... </h2>
    ''', 200


# @app.route('/login/<username>/<passwordhash>', methods=['GET', 'POST'])
@app.route('/login')
def login():
    return render_template('login.html')


def google_oauth_callback():
    pass


def forget_password():
    pass
