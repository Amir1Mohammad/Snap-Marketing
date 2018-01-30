#!/usr/bin/env python
# -*- coding: utf-8 -*-
# find . -name "*.pyc" -exec rm -rf {} \;

__Author__ = "Amir Mohammad"

# project imports :
from flask import render_template
from application import app


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/signup')
def add_peyk():
    return render_template('signup.html')


@app.route('/submit')
def wait_time():
    return render_template('submit.html')


@app.route('/sos')
def sos():
    return render_template('sos.html')


@app.route('/location')
def location():
    return render_template('location.html')


@app.route('/yek')
def yek():
    return render_template('yek.html')


@app.route('/sitemap')
def sitemap():
    return render_template('sitemap.html')


@app.route('/help')
def help():
    return render_template('help.html')


@app.route('/beh')
def beh():
    return render_template('beh.html')
