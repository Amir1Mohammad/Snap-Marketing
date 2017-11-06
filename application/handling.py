#!/usr/bin/env python
# -*- coding: utf-8 -*-
# find . -name "*.pyc" -exec rm -rf {} \;

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
