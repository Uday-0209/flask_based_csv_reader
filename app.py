from flask import Flask

app = Flask(__name__)

@app.route('/')

def new():
    return "<p> new app </p>"