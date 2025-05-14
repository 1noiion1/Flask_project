from flask import Flask

app = Flask(__name__)

#1
@app.route('/hello')
def hello():
    return f'Hello, world!'

@app.route('/info')
def info():
    return f'This is an informational page'


#2
@app.route('/calc/<int:numb_1>/<int:numb_2>')
def calc(numb_1, numb_2):
    return f'The sum of {numb_1} and {numb_2} is {numb_1 + numb_2}'


#3
@app.route('/reverse/<text>')
def reverse(text):
    if len(text) < 1 or text == ' ':
        return 'There are too few characters'
    else:
        return text[::-1]


#4
@app.route('/user/<name>/<int:age>')
def user(name, age):
    if age <= 0:
        return 'You are too small'
    else:
        return f'Hello, {name}. You are {age} years old'


if __name__ == "__main__":
    app.run(debug=True)