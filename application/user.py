#!/usr/bin/env python
# -*- coding: utf-8 -*-
# find . -name "*.pyc" -exec rm -rf {} \;

# Python import:
from flask_login import LoginManager

__Author__ = "Amir Mohammad"

# Project import :
from application import app
from models.user import User
from models.base import db
from handling import create_id_user


@app.route('/su/<email>/<passwordhash>/<firstname>/<lastname>/<gender>/<birth_date>/<phones>',
           methods=['GET', 'POST'])
def signup(email, passwordhash, firstname, lastname, gender, birth_date, phones):
    g = User(id=create_id_user(), email=email, passwordhash=passwordhash, firstname=firstname, lastname=lastname,
             gender=gender, birth_date=birth_date, phones=phones)
    db.session.add(g)
    db.session.commit()
    return '''
    <h3>User added Completely ... </h3>
    ''',200



@app.route('/login/<username>/<passwordhash>', methods=['GET', 'POST'])
def login():
    pass


def google_oauth_callback():
    pass

@app.route("/logout/<username>")
def logout():
    pass


def forget_password():
    pass


