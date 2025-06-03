from flask import render_template, request, redirect, url_for
from app import app

valid_mail = ('@mail.ru', '@mail.com', '@bk.ru', '@yandex.ru', '@rambler.ru',
              '@live.ru', '@hotmail.com', '@gmail.com', '@icq.com', '@qip.ru')

@app.route('/')
def form():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/submit', methods=["POST", "GET"])
def submit():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        if email.endswith(valid_mail) is False:
            return "Invalid email format"
        else:
            return render_template("result.html", name=name, email=email, message=message)

    else:
        return redirect(url_for("index"))


