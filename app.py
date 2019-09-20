import json
import os

from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from werkzeug.utils import secure_filename

import sys

app = Flask(__name__)
Bootstrap(app)

lines=[]
with open('static/files.txt','r') as f:
    lines = f.read().split("\n")

@app.route('/', methods=["GET"])
def index():
    return render_template('index.html', value=0)


@app.route('/', methods=["POST"])
def index_post():
    safe_fn = lines[int(request.form["idx"])]
    filename, file_extension = os.path.splitext(safe_fn)
    txt_fn = filename + ".txt" 
    f=open(txt_fn, 'w')
    f.write(request.form["val"])
    f.close()
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