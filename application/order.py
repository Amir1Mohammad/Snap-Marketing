#!/usr/bin/env python
# -*- coding: utf-8 -*-
# find . -name "*.pyc" -exec rm -rf {} \;
from os import abort

__Author__ = "Amir Mohammad"

# python import :
from flask import jsonify

# project import :
from application import app
from models.order import Order
from models.base import db
from handling import create_id_order


@app.route('/so/<locate_source>', methods=['GET'])
def see_orders(locate_source):
    listme = []
    o = Order.query.filter_by(locate_source=locate_source).all()
    for row in o:
        show = {
            'id': row.id,
            'source_id': row.source_id,
            'locate_source': row.locate_source,
            'orders': row.orders,
            'status': row.status,
            'start_at': row.start_at
        }
        listme.append(show)
    return jsonify(jsonify=listme)


@app.route('/ao/<source_id>/<locate_source>/<orders>/<status>', methods=['GET', 'POST'])
def add_order(source_id, locate_source, orders, status):
    o = Order(id=create_id_order(), source_id=source_id, locate_source=locate_source, orders=orders,
              status=status)
    db.session.add(o)
    db.session.commit()
    return '''
    <h3>Orders added Completely ... </h3>
    '''

