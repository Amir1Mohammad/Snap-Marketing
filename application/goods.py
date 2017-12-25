#!/usr/bin/env python
# -*- coding: utf-8 -*-
# find . -name "*.pyc" -exec rm -rf {} \;

__Author__ = "Amir Mohammad"

# python imports:
from flask import jsonify

# project import :
from application import app
from models.goods import Good
from application.extension import db
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


@app.route('/category', methods=['GET'])
def see_category():
    listme = []
    h = Good.query.order_by(Good.category).all()
    print h
    for each in h:
        show = {
            'category': each.category,

        }
        if show not in listme:
            listme.append(show)

    return jsonify(categories=listme)


@app.route('/property/<category>',methods=['GET'])
def see_property():
    pass


# simple input http://0.0.0.0:8000/ag/pofak/lina/loole/2000
@app.route('/ag/<name>/<category>/<property>/<cost>', methods=['GET', 'POST'])
def add_goods(name, category, property, cost):
    g = Good(id=create_id_good(), name=name, category=category, property=property, cost=int(cost))
    db.session.add(g)
    db.session.commit()
    return '''
            <h2>Good added Completely ... </h2>
    '''


