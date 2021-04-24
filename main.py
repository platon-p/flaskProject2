import hashlib
from datetime import datetime

from flask import Flask, request, render_template, redirect
from flask_login import LoginManager, login_user, current_user, login_required, logout_user

from cards import *
from data.db_session import create_session, global_init
from data.users import User
from data.results import association_table
from forms import *

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def hello_world():
    # обработка перехода на главную страницу
    cards = [MainCards('shapes.svg', 'Математика', 'math'), MainCards('magnet.svg', 'Физика', 'physics'),
             MainCards('computer.svg', 'Информатика', 'computers')]
    # передаем список из карточек предметов
    return render_template('ind.html', title='Моя школа', cards=cards)


@app.errorhandler(404)
def page_not_found(e):
    # обработка страницы ошибки 404
    return render_template('404.html')


@login_manager.user_loader
def load_user(user_id):
    db_sess = create_session()
    return db_sess.query(User).get(user_id)


@app.route('/logout')
@login_required
def logout():
    # обработка выхода из аккаунта
    logout_user()
    return redirect("/")


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=True)
            return redirect("/")
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/math')
def math_lesson():
    # переход на страницу математики
    cards = CARDS['math']
    return render_template('lesson.html', title='Математика', cards=cards)


@app.route('/physics')
def ph_lesson():
    # переход на страницу физики
    cards = CARDS['physics']
    return render_template('lesson.html', title='Физика', cards=cards)


@app.route('/computers')
def inf_lesson():
    cards = CARDS['computers']
    return render_template('lesson.html', title='Информатика', cards=cards)


@app.route('/math/sequences')
def sequences_lesson():
    # переход на страницу с последовательностями
    for i in CARDS['math']:
        if i.link == '/math/sequences':
            # выбираем ту карточку, которая соответствует теме
            print(current_user.id)
            return render_template('sequences.html', card=i)
    return '404 error'


@app.route('/math/sequences/test', methods=['GET', 'POST'])
def test_sequences():
    form = TestStereometry()
    if form.validate_on_submit():
        return 'Данные успешно сохранены'
    return render_template('tests.html', form=form, title='Математика', link='math', link2='sequences')


@app.route('/math/stereometry')
def stereometry_lesson():
    # переход на страницу с последовательностями
    for i in CARDS['math']:
        if i.link == '/math/stereometry':
            # выбираем ту карточку, которая соответствует теме
            print(current_user.id)
            return render_template('stereometry.html', card=i)
    return '404 error'


@app.route('/math/stereometry/test', methods=['GET', 'POST'])
def test_stereometry():
    form = SequencesTest()
    if form.validate_on_submit():
        return 'Данные успешно сохранены'
    return render_template('tests.html', form=form, title='Математика', link='math', link2='stereometry')


@app.route('/physics/atomic-structure')
def atomic_structure_lesson():
    for i in CARDS['physics']:
        if i.link == '/physics/atomic-structure':
            print(current_user.id)
            return render_template('atomic-structure.html', card=i)
    return '404 error'


@app.route('/physics/atomic-structure/test', methods=['GET', 'POST'])
def test_atomic_structure():
    form = AtomTest()
    if form.validate_on_submit():
        return 'Данные успешно сохранены'
    return render_template('tests_atomic-structure.html', form=form)


@app.route('/physics/elec')
def elec_lesson():
    for i in CARDS['physics']:
        if i.link == '/physics/elec':
            print(current_user.id)
            return render_template('elec.html', card=i)
    return '404 error'


@app.route('/physics/elec/test', methods=['POST', 'GET'])
def test_elec():
    form = TestElec()
    if form.validate_on_submit():
        return "Данные успешно сохранены"
    return render_template('tests.html', form=form, title='Физика', link='physics', link2='elec')


@app.route('/computers/binary')
def binary_lesson():
    for i in CARDS['computers']:
        if i.link == '/computers/binary':
            print(current_user.id)
            return render_template('binary.html', card=i)
    return '404 error'


@app.route('/computers/binary/test', methods=['POST', 'GET'])
def test_binary():
    form = TestBinary()
    if form.validate_on_submit():
        return 'Данные успешно сохранены'
    return render_template('tests.html', form=form, title='Информатика', link='computers', link2='binary')


@app.route('/computers/cpu')
def cpu_lesson():
    for i in CARDS['computers']:
        if i.link == '/computers/cpu':
            print(current_user.id)
            return render_template('cpu.html', card=i)
    return '404 error'


@app.route('/computers/cpu/test', methods=['POST', 'GET'])
def test_cpu():
    form = TestCPU()
    if form.validate_on_submit():
        # вот тут надо сделать
        print(request.form["current_user"])
        res = check_test(form, request.form["current_user"], "Процессор")
        return f'Вы прошли тест на {res} данные успешно сохранены'
    return render_template('tests.html', form=form, title='Информатика', link='computers', link2='cpu')


@app.route("/registration", methods=['POST', 'GET'])
def registration():
    form = RegisterForm()
    if form.validate_on_submit():
        db_sess = create_session()
        req = db_sess.query(User).filter(User.email == form.mail.data)
        if len(form.password.data) >= 8 and len(list(req)) < 1:
            user = User()
            user.surname = form.surname.data
            user.name = form.name.data
            user.email = form.mail.data
            user.password = hashlib.md5(bytes(form.password.data.encode("utf-8"))).hexdigest()
            user.modified_date = datetime.now()
            db_sess.add(user)
            db_sess.commit()
            return redirect("/login")
    return render_template('registration.html', title='Регистрация', form=form)


@app.route("/profile/<int:user_id>")
def profile(user_id):
    print(request.user_id)


def check_test(form, user_id, name):
    count = 0
    for i, j in enumerate(form):
        if len(form.answers) > i:
            if j == form.answers[i]:
                count += 1
        else:
            break
    db_sess = create_session()
    result = association_table()
    result.user_id = user_id
    result.lessons_name = name
    result.percent = f"{count}/{len(form.answers)}"
    db_sess.add(result)
    db_sess.commit()
    return f"{count}/{len(form.answers)}"


if __name__ == '__main__':
    global_init("db/project.db")
    app.run(debug=True)
