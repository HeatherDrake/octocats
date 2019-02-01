import os

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello():

    index_file = open('index.html', 'r')
    my_html = index_file.read()
    index_file.close()

    return my_html