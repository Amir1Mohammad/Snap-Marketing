# -*- coding: utf-8 -*-


# imports
from datetime import datetime
from base import db

__author__ = 'Amir Mohammad'


class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, nullable=False, primary_key=True)
    source_id = db.Column(db.Integer, nullable=False)
    locate_source = db.Column(db.String(256), nullable=False)
    orders = db.Column(db.String(256), nullable=False)
    start_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    end_at = db.Column(db.DateTime, nullable=True,default=datetime.utcnow)
    status = db.Column(db.Boolean, nullable=False)
