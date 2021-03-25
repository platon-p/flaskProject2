from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('ind.html')


@app.route('/login')
def login():
    return render_template('reg.html')


@app.route('/math')
def math_lesson():
    return render_template('lessonM.html')


@app.route('/physics')
def ph_lesson():
    return render_template('lessonPh.html')


if __name__ == '__main__':
    app.run(debug=True)
