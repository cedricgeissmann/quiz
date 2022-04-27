#! /usr/bin/env python
from flask import Flask, render_template
import json
from random import choice

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True





@app.route("/")
def home():
    return render_template("index.html")






@app.route("/salome")
def salome():
    return render_template("Salome.html")

@app.route("/anja")
def anja():
    return render_template("Anja.html")




if __name__ == "__main__":
    app.run()
