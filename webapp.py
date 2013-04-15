#!/usr/bin/env python
# coding: utf-8

"""
  http://www.github.com/erylee/tango
  ~~~~~~~
  Enterprise Web Application Framework
  :copyright: (c) 2013 by Ery Lee(ery.lee at gmail.com)
"""

from flask import Flask, redirect, url_for, \
    render_template, g, request, abort, current_app

app = Flask(__name__)
app.config.from_pyfile('setting.py')

app.debug = True

@app.route("/")
def index():
    return render_template("/index.html")

if __name__ == "__main__":
    app.run()

