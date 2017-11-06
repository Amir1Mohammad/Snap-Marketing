#!/usr/bin/env python
# -*- coding: utf-8 -*-
# find . -name "*.pyc" -exec rm -rf {} \;

__Author__ = "Amir Mohammad"

# python import :


# project import :
from application import app


@app.errorhandler(404)
def page_not_found(e):
    print "url not found , 404"
    return '''
    <h1>The url not found ...</h1>
    <h3>Check it again . tnx ...</h3>
    ''', 404
