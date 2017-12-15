# -*- coding: utf-8 -*-


# project imports
from application.extension import db

__author__ = 'Amir Mohammad'


class Good(db.Model):
    __tablename__ = 'goods'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    category = db.Column(db.String(25), nullable=False)
    property = db.Column(db.String(25), nullable=False)
    cost = db.Column(db.Integer, nullable=False)
