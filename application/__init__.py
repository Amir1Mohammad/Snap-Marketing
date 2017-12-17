from flask import Flask

app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.config['SECRET_KEY'] = 'topsecret'
__Author__ = "Amir Mohammad"


from application import goods, order, peyk, fof, user, cost, dashboard
