from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from models import User


app = Flask(__name__)
app.config['DEBUG'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = Config.DATABASE_URI

db = SQLAlchemy(app)
session = db.session


@app.teardown_appcontext
def shutdown_session(exception=None):
    print 'removing db session'
    session.remove()


@app.route("/")
def hello():
    context = User.query.all()
    return "Hello World!" + context
