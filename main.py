from datetime import datetime

from flask import Flask, request, render_template, redirect
from flask_login import LoginManager, login_user
from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, BooleanField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired

from data.db_session import create_session, global_init
from data.tests import Lessons
from data.users import User

# from tests import TestForm

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def hello_world():
    return render_template('ind.html', title='Моя школа')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', title="Упс... Ошибочка(")


class LoginForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


@login_manager.user_loader
def load_user(user_id):
    db_sess = create_session()
    return db_sess.query(User).get(user_id)


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = create_session()
        db_sess = create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
    return render_template('reg.html', title='Авторизация', form=form)


@app.route('/math')
def math_lesson():
    return render_template('lessonM.html', title='Математика')


@app.route('/math/sequences')
def sequences_lesson():
    return render_template('sequences.html', title="Последовательности")


@app.route('/math/stereometry')
def stereometry_leson():
    return render_template('stereometry.html')


@app.route('/physics')
def ph_lesson():
    return render_template('lessonPh.html', title='Физика')


@app.route('/physics/atomic-structure')
def atomic_structure_leson():
    return render_template('atomic-structure.html')


@app.route('/physics/elec')
def elec_leson():
    return render_template('elec.html')


@app.route('/physics/atomic-structure/test')
def test_atomic_structure():
    return render_template('tests-atomic-structure.html')


@app.route('/physics/elec/test', methods=['POST', 'GET'])
def test_elec():
    if request.method == 'GET':
        return render_template('test_elec.html')
    elif request.method == 'POST':
        answers = list(request.form[i] for i in request.form.keys())[1:-1]
        db_sess = create_session()
        req = db_sess.query(Lessons).filter(Lessons.path_to_html == "test_elec.html").first().answers
        f = open(req, mode="r", encoding="utf-8")
        answers_true = [i.strip() for i in f.readlines()]
        f.close()
        return render_template("finish_test.html", answers_true=answers_true, answers=answers, len=len(answers_true))


@app.route('/computers')
def inf_lesson():
    return render_template('lessonI.html', title='Информатика')


@app.route('/computers/binary')
def binary_lesson():
    return render_template('binary.html')


@app.route('/computers/cpu')
def cpu_lesson():
    return render_template('cpu.html')


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
            db_sess = create_session()
            req = db_sess.query(User).filter(User.email == request.form["email"])
            if 5 <= int(request.form["age"]) <= 100 \
                    and 1 <= int(request.form["school_class"]) <= 11 \
                    and len(request.form["password"]) >= 8 and len(list(req)) < 1:
                user = User()
                user.surname = request.form["surname"]
                user.name = request.form["name"]
                user.email = request.form["email"]
                user.password = hash(request.form["password"])
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


@app.route("/profile/<int:user_id>")
def profile(user_id):
    user = load_user(user_id)
    return render_template('profile.html', user=user)


if __name__ == '__main__':
    global_init("db/project.db")
    app.run(debug=True)
