# -*- coding: utf-8 -*-


# project imports
from base import db

__author__ = 'Amir Mohammad'


class Good(db.Model):
    __tablename__ = 'goods'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    category = db.Column(db.Enum('Dairy', 'Junk', 'Food'), nullable=False)
    property = db.Column(db.String(25), nullable=False)
    cost = db.Column(db.Integer, nullable=False)
