# -*- coding: utf-8 -*-

# python imports
from datetime import datetime

# project import
from application.extension import db

__author__ = 'Amir Mohammad'


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, nullable=False)
    passwordhash = db.Column(db.String(64), nullable=False)
    firstname = db.Column(db.Unicode(254))
    lastname = db.Column(db.Unicode(254))
    gender = db.Column(db.Enum('Male', 'Female', name='gender'), default='Male', nullable=True)
    register_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    birth_date = db.Column(db.String(10), nullable=True)
    phones = db.Column(db.BigInteger, nullable=False)
