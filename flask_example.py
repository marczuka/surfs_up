from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def welcome():
    return ("Hello world!")