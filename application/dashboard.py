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