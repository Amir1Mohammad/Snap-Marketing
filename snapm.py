#!/usr/bin/env python
# -*- coding: utf-8 -*-
# find . -name "*.pyc" -exec rm -rf {} \;

__Author__ = "Amir Mohammad"

from flask_script import Manager
from application import app


manager = Manager(app)
from database import manager as database_manager
manager.add_command("database", database_manager)

@manager.command
def run():
    """
    run server on port 8000 and domain name is ...
    """
    app.run(host='0.0.0.0', port=8000, debug=True)


if __name__ == '__main__':
    manager.run()