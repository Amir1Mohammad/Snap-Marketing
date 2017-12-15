#!/usr/bin/env python
# -*- coding: utf-8 -*-
# find . -name "*.pyc" -exec rm -rf {} \;

# python import:
import bcrypt

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


def get_hash(password):
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    return hashed


def check_hash(password, hashed):
    if bcrypt.checkpw(password, hashed):
        print("It Matches!")
    else:
        print("It Does not Match :(")


# simple Calling function
# avr = get_hash('amir mohammad mohammadi')
# check_hash('amir mohammad mohammadi',avr)

