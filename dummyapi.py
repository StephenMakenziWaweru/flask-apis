#!/usr/bin/env python3
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({'hello': 'Hello World!'})

if __name__ == '__main__':
    app.run(debug=True)
