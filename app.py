import json
import os

from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)


@app.route('/', methods=["GET"])
def index():
    return render_template('index.html', value=0)


@app.route('/', methods=["POST"])
def index_post():
    data_ = request.get_data(as_text=True)
    data = data_.split('.jpg')
    txt = data[0] + ".txt"
    result = data[1]

    with open(txt, 'w') as f:
        f.writelines(result)
        
    return "200 OK"


@app.route('/', methods=['DELETE'])
def index_del():
    data_ = request.get_data(as_text=True)
    data = data_.split("\n")
    txt = data[0].replace(".jpg",'.txt')
    line = int(data[1])
    content = []
    with open(txt, 'r') as f:
        content = f.readlines()
        del(content[line])
        
    with open(txt, 'w') as f:
        f.writelines(content)

    return "200 OK"

@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


if __name__ == '__main__':
    app.run(debug=True)
