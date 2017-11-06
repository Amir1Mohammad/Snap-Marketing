#!/usr/bin/env python
# -*- coding: utf-8 -*-
# find . -name "*.pyc" -exec rm -rf {} \;

__Author__ = "Amir Mohammad"

# project import :
from application import app
from models.user import User
from models.base import db
from handling import create_id_user


@app.route('/su/<email>/<password>/<firstname>/<lastname>/<gender>/<birth_date>/<phones>'
    ,methods=['POST'])
def signup(email, password, firstname, lastname, gender, birth_date, phones):
    g = User(id=create_id_user(), email=email, password=password, firstname=firstname, lastname=lastname,
             gender=gender, birth_date=birth_date, phones=phones)
    db.session.add(g)
    db.session.commit()
    return '''
    <h3>User added Completely ... </h3>
    '''


def login():
    pass


def google_oauth_callback():
    pass


def logout():
    pass


def forget_password():
    pass
