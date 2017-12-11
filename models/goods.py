# -*- coding: utf-8 -*-


# project imports
from base import db

__author__ = 'Amir Mohammad'


class Good(db.Model):
    __tablename__ = 'goods'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(254), nullable=False)
    category = db.Column(db.Unicode(254), nullable=False)
    property = db.Column(db.Unicode(254), nullable=False)
    cost = db.Column(db.Integer, nullable=False)
