from datetime import datetime

from flask import Flask, request, render_template

from data.db_session import create_session, global_init
from data.users import User

# from tests import TestForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def hello_world():
    return render_template('ind.html', title='Моя школа')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('reg.html')
    elif request.method == 'POST':
        global_init("db/project.db")
        db_sess = create_session()
        req = db_sess.query(User).filter(User.email == "".join(request.form["mail_input"]))
        if len(list(req)) == 1:
            user = list(req)[0]
            password = user.password
            if password == "".join(request.form["password_input"]):
                return render_template('ind.html', user_id=user.id,
                                       user_surname=user.surname,
                                       user_name=user.name)


@app.route('/math')
def math_lesson():
    return render_template('lessonM.html', title='Математика')


@app.route('/math/sequences')
def sequences_lesson():
    return render_template('sequences.html')


@app.route('/physics')
def ph_lesson():
    return render_template('lessonPh.html', title='Физика')


@app.route('/physics/atomic-structure')
def atomic_structure_leson():
    return render_template('atomic-structure.html')


@app.route('/physics/atomic-structure/test')
def test_atomic_structure():
    return render_template('tests-atomic-structure.html')


@app.route('/computers')
def inf_lesson():
    return render_template('lessonI.html', title='Информатика')


@app.route('/computers/binary')
def binary_lesson():
    return render_template('binary.html')


@app.route('/computers/cpu')
def cpu_lesson():
    return render_template('cpu.html')


@app.route('/physics/elec/test', methods=['POST', 'GET'])
def test_elec():
    if request.method == 'GET':
        return render_template('test_elec.html')
    elif request.method == 'POST':
        print(request.form["one"])
        return "Форма отправлена"


# @app.route('/bib', methods=['GET', 'POST'])
# def bib():
#     form = TestForm()
#     if form.validate_on_submit():
#         return "Форма отправлена"
#     return render_template('test.html', form=form)


@app.route("/registration", methods=['POST', 'GET'])
def registration():
    if request.method == 'GET':
        return render_template('registration.html', title='Моя школа')
    elif request.method == 'POST':
        try:
            global_init("db/project.db")
            db_sess = create_session()
            req = db_sess.query(User).filter(User.email == request.form["email"])
            if 5 <= int(request.form["age"]) <= 100 \
                    and 1 <= int(request.form["school_class"]) <= 11 \
                    and len(request.form["password"]) >= 8 and len(list(req)) < 1:
                user = User()
                user.surname = request.form["surname"]
                user.name = request.form["name"]
                user.email = request.form["email"]
                user.password = request.form["password"]
                user.age = request.form["age"]
                user.school_class = request.form["school_class"]
                user.modified_date = datetime.now()
                user.admin = False
                db_sess.add(user)
                db_sess.commit()
                return render_template("reg_final.html")
            else:
                return render_template('registration.html')
        except Exception:
            return render_template('registration.html')


@app.route("/profile")
def profile():
    print(request.user_id)


if __name__ == '__main__':
    app.run(debug=True)
