#!/usr/bin/env python
# -*- coding: utf-8 -*-
# find . -name "*.pyc" -exec rm -rf {} \;

__Author__ = "Amir Mohammad"

# python imports:
from flask import jsonify

# project import :
from application import app
from models.goods import Good
from models.base import db
from garbage import create_id_good


@app.route('/sg', methods=['GET'])
def see_goods():
    lisle = []
    o = Good.query.filter_by().all()
    for each in o:
        show = {
            'id': each.id,
            'name': each.name,
            'category': each.category,
            'property': each.property,
            'cost': each.cost

        }
        lisle.append(show)
    return jsonify(jsonify=lisle)


@app.route('/ag/<name>/<category>/<property>/<cost>', methods=['GET', 'POST'])
def add_goods(name, category, property, cost):
    g = Good(id=create_id_good(), name=name, category=category, property=property, cost=int(cost))
    db.session.add(g)
    db.session.commit()
    return '''
            <h3>Good added Completely ... </h3>
    '''
