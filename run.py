#! /usr/bin/env python
from flask import Flask, render_template, request
import json
from random import choice
from geopy.distance import distance

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


def random_question():
    with open("questions.json", 'r') as f:
        questions = json.load(f)
    return choice(questions)

def check_answer(q_id, a_id):
    with open("questions.json", 'r') as f:
        questions = json.load(f)
    q = list(filter(lambda x: x["id"] == q_id, questions))[0]
    return q["correct"] == a_id


def calc_distance(loc_1, loc_2):
    loc_1 = loc_1.split(",")
    loc_2 = loc_2.split(",")
    dist = distance(loc_1, loc_2)
    return dist


def check_location(q_id, loc):
    with open("questions.json", 'r') as f:
        questions = json.load(f)
    q = list(filter(lambda x: x["id"] == int(q_id), questions))[0]
    dist = calc_distance(q["answer"], loc)
    return dist



@app.route("/")
def home():
    return render_template("index.html")


@app.route("/question")
def question():
    return render_template("question.html", question=random_question())


@app.route("/answer/<int:question_id>/<int:answer_id>")
def answer(question_id, answer_id):
    correct = check_answer(question_id, answer_id)
    return render_template("answer.html", correct=correct)


@app.route("/send-loc")
def send_loc():
    q_id = request.args["question_id"]
    loc = request.args["loc"]
    dist = check_location(q_id, loc)
    return render_template("answer.html", dist=dist)


if __name__ == "__main__":
    app.run()
