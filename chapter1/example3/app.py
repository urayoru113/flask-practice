from flask import Flask
from flask import escape

app = Flask(__name__)

@app.route("/hello/<name>")
def hello(name):
    return 'hello <strong>{}</strong>'.format(escape(name))
