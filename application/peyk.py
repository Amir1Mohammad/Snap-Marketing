#!/usr/bin/env python
# -*- coding: utf-8 -*-
# find . -name "*.pyc" -exec rm -rf {} \;

__Author__ = "Amir Mohammad"

# project import:
from application import app
from models.base import db


@app.route('/accept/<id>', methods=['POST','GET'])
def accept_order(id):
    from models.order import Order
    s = Order.query.filter_by(id=id).first()
    s.status = 1
    db.session.commit()
    return '''
    <h3> Status state is changed ...</h3>
    '''

