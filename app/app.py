from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>hello flask the from the behnd</h1>"
