#!/usr/bin/env python
# -*- coding: utf-8 -*-
# find . -name "*.pyc" -exec rm -rf {} \;

# python import:
from werkzeug.security import generate_password_hash, check_password_hash

__Author__ = "Amir Mohammad"


def create_id_order():
    from random import randint
    ic = randint(10000, 100000)
    return ic


def create_id_user():
    from random import randint
    ic = randint(20000, 2000000)
    return ic


def create_id_good():
    from random import randint
    ic = randint(1, 1000)
    return ic


def create_id_peyk():
    from random import randint
    ic = randint(3000, 30000)
    return ic


def set_hashing(password):
    pw_hash = generate_password_hash(password)
    print pw_hash
    return pw_hash


def check_hashing(normal, hashing):
    print check_password_hash(normal, hashing)
    return check_password_hash(normal, hashing)


set_hashing('amir')
# check_hashing('amir', 'pbkdf2:sha1:1000$hhA4BVtu$40127ac47d6157f5cfdf89893f9e1ba73aeb9e05')





# class Pass(object):
#     def __init__(self, username, password):
#         self.username = username
#         self.set_password(password)
#
#     def set_password(self, password):
#         self.pw_hash = generate_password_hash(password)
#
#     def check_password(self, password):
#         return check_password_hash(self.pw_hash, password)
#
#
# me = Pass('amir mohammad', 'amir0010')
# print me.pw_hash
# 'sha1$Z9wtkQam$7e6e814998ab3de2b63401a58063c79d92865d79'
# print me.check_password('amir0010')
# print me.check_password('amir')
