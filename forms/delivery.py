#!/usr/bin/env python
# -*- coding: utf-8 -*-
# find . -name "*.pyc" -exec rm -rf {} \;



__author__ = 'Amir Mohammad'

from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required


class DeliveryMan(Form):
    firstname = StringField('What is your first name?', validators=[Required()])
    lastname = StringField('What is your first name?', validators=[Required()])
    # address
    # phone
    # mobile
    # account number
    # birth_Date
    # married
    # image su pishine
    # image generate 1
    # image generate 2
    # image show face
    # image cart melli
    # rah ashnayi
    # username
    # password
    # email
    # about
    #

    submit = SubmitField('Submit')


