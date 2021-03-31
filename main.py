from flask import Flask
from flask import render_template, url_for

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


@app.route('/computers')
def inf_lesson():
    return render_template('lessonI.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
