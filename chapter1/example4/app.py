from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/hi")
@app.route("/hello")
@app.route("/cat")
def hello():
    ret = """
    <h1>CAT!!!</h1>
    <div><img src="https://i.imgur.com/4AiXzf8.jpeg"></div>
    """
    return ret
