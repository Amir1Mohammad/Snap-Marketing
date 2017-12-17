# -*- coding: utf-8 -*-


# flask imports
from flask_script import Manager, prompt_bool

# project imports
from application.extension import db

__author__ = 'Amir Mohammad'

manager = Manager(usage="Perform database operations")


@manager.command
def drop():
    """Drops database tables"""
    if prompt_bool("Are you sure you want to lose all your data"):
        db.drop_all()


@manager.command
def create():
    """Create all the tables"""
    db.create_all()


@manager.command
def recreate():
    """Recreates database tables (same as issuing 'drop' and then 'create')"""
    drop()
    create()


@manager.command
def test():
    """Use it for test purpose"""
    pass

