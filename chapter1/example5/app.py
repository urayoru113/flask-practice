from flask import Flask
from flask import url_for, redirect

app = Flask(__name__)

@app.route("/cat")
def cat():
    ret = """
    <h1>CAT!!!</h1>
    <div><img src="https://i.imgur.com/4AiXzf8.jpeg"></div>
    """
    return ret

@app.route("/dog")
def dog():
    return redirect(url_for('cat'))
