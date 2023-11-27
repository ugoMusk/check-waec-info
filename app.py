#!/usr/bin/env python3
"""
module defining our api endpoints
"""
import os
import sys
modelPath = os.path.abspath("./")
sys.path.append(modelPath)
from flask import Flask, jsonify, send_file, render_template, url_for, redirect, request
from flask_compress import Compress
import json
import base64
import chardet

app = Flask(__name__)

compress = Compress()
compress.init_app(app)


# @app.route("/", methods=['GET', 'POST'], strict_slashes=False)
@app.route("/")
def homePage():
    """ 
    home route
    """

    return render_template("home.html")


if __name__ == "__main__":
    app.run()
