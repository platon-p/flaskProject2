from flask import Flask, request, url_for
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


@app.route('/computers')
def inf_lesson():
    return render_template('lessonI.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), e


@app.route('/physics/atomic-structure/test')
def test_atomic_structure():
    return render_template('tests-atomic-structure.html')


@app.route('/physics/elec/test', methods=['POST', 'GET'])
def test_elec():
    if request.method == 'GET':
        return render_template('test_elec.html')
    elif request.method == 'POST':
        print(request.form["q1"])
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(debug=True)
