from flask import render_template, request, redirect, url_for
from app import app
import random

list_joke = ["God gave man teeth so that he could live, and toothache so that he would clearly know his place..",
             "Everything happens the first time, but not everything happens the second time..",
             "Why do birds fly south in winter? - Because flying is faster than walking..",
             "If you are imprisoned for tax evasion, you will be held for taxes that you have not already paid..",
             "I had a fit of vivacity this morning. But he attacked the wrong one…"]


@app.route('/')
def form():
    return render_template('form.html')


@app.route('/submit', methods=["POST", "GET"])
def submit():
    if request.method == "POST":
        name = request.form.get("name")
        color = request.form.get("color")
        profession = request.form.get("profession")
        hobbies = request.form.getlist("hobbies")
        level = request.form.get("level")

        if not name:
            error_message = "We can't process your form without your name, Mr. Anonymous!"
            return error_message

        elif not color:
            error_message = "We are very interested in what your favorite color is, please indicate it!"
            return error_message

        elif not profession:
            error_message = "Are you unemployed?"
            return error_message

        elif not hobbies:
            error_message = "What about your hobby?"
            return error_message

        elif not level:
            error_message = "You didn't specify your level."
            return error_message

        joke = random.choice(list_joke)
        return render_template("result.html", name=name, color=color,
                               profession=profession, hobbies=hobbies, level=level, joke=joke)

    else:
        return redirect(url_for("form"))


