#!/usr/bin/env python3
from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        some_json = request.get_json()
        return jsonify({'You sent': some_json})
    else:
        return jsonify({"greet": "Hello World"})

@app.route('/multi/<int:num>', methods=['GET', 'POST'])
def get_multiply(num):
    return jsonify({'result': num * 10})

if __name__ == '__main__':
    app.run(debug=True)
