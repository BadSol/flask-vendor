from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run('192.168.33.33', 8000)  # remove argument to run on local host
