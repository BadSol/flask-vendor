from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.config['DEBUG'] = True

# secrets = None
with open('SECRETS.json') as data_file:
    secrets = json.load(data_file)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://{}:{}@localhost/{}'.format(
    secrets["db_user"],
    secrets["db_password"],
    secrets["db_name"])

Base = SQLAlchemy(app)


@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run('192.168.33.33', 8000)  # remove argument to run on local host
