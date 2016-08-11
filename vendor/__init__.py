from flask import Flask
from database import db_session

app = Flask(__name__)
app.config['DEBUG'] = True


@app.teardown_appcontext
def shutdown_session(exception=None):
    print 'removing db session'
    db_session.remove()


@app.route("/")
def hello():
    return "Hello World!"
