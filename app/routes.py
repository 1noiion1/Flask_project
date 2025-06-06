from flask import render_template, request, redirect, url_for
from app import app
from datetime import datetime

valid_mail = ('@mail.ru', '@mail.com', '@bk.ru', '@yandex.ru', '@rambler.ru',
              '@live.ru', '@hotmail.com', '@gmail.com', '@icq.com', '@qip.ru')

@app.route('/')
def form():
    current_time = datetime.now()
    return render_template('index.html', current_time=current_time)


@app.route('/contact')
def contact():
    contact_info = {
        'customer_service': {
            'name': 'Elena Ivanova',
            'position': 'Head of Customer Care Department',
            'phone': '+7 (495) 123-45-67',
            'email': 'support@company.com'
        },
        'address': {
            'street': 'Pushkin St., 10',
            'city': 'Moscow',
            'postal_code': '123456'
        }
    }

    return render_template('contact.html', contact_info=contact_info)


@app.route('/about')
def about():
    team_members = [
        {'name': 'Alice', 'role': 'Developer'},
        {'name': 'Bob', 'role': 'Designer'},
        {'name': 'Charlie', 'role': 'Project Manager'}
    ]
    return render_template('about.html', team=team_members)

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


