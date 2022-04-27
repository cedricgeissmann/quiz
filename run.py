#! /usr/bin/env python
from flask import Flask, render_template


app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route("/index")
def home():
    return render_template("index.html")

@app.route("/spielanleitung")
def spielanleitung():
    return render_template("Spielanleitung.html")


@app.route("/irem")
def irem():
    return render_template("Irem.html")

@app.route("/olivia")
def olivia():
    return render_template("Olivia.html")

@app.route("/creators")
def creators():
    return render_template("Creators.html")

@app.route("/lilia")
def lilia():
    return render_template("Lilia.html")



if __name__ == "__main__":
    app.run()
