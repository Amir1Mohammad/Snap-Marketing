from flask.ext.sqlalchemy import SQLAlchemy
from application import app

db = SQLAlchemy()
db.init_app(app)
