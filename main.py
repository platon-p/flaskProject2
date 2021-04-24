import hashlib
from datetime import datetime

from flask import Flask, render_template, redirect
from flask_login import LoginManager, login_user, current_user, login_required, logout_user

from cards import *
from data.db_session import create_session, global_init
from data.results import Result
from data.users import User
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


@app.errorhandler(500)
def error500():
    # обработка страницы ошибки 500
    return render_template('something_wrong.html', text='Внутренняя ошибка сервера')


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


@app.route('/enter_please')
def enter():
    return render_template('enter_please.html')


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
            return render_template('sequences.html', card=i)
    return '404 error'


@app.route('/math/sequences/test', methods=['GET', 'POST'])
def test_sequences():
    try:
        form = TestSequences()
        if current_user.id:
            if form.validate_on_submit():
                res = check_test(form, current_user.id, "Последовательности")
                return render_template('something_wrong.html', text='Данные успешно сохранены')
            return render_template('tests.html', form=form, title='Математика', link='math', link2='sequences')
    except Exception:
        return redirect("/enter_please")


@app.route('/math/stereometry')
def stereometry_lesson():
    # переход на страницу с последовательностями
    for i in CARDS['math']:
        if i.link == '/math/stereometry':
            # выбираем ту карточку, которая соответствует теме
            return render_template('stereometry.html', card=i)
    return '404 error'


@app.route('/math/stereometry/test', methods=['GET', 'POST'])
def test_stereometry():
    try:
        form = TestStereometry()
        if current_user.id:
            if form.validate_on_submit():
                res = check_test(form, current_user.id, "Стереометрия")
                return render_template('something_wrong.html', text='Данные успешно сохранены')
        return render_template('tests.html', form=form, title='Математика', link='math', link2='sequences')
    except Exception:
        return redirect("/enter_please")


@app.route('/physics/atomic-structure')
def atomic_structure_lesson():
    for i in CARDS['physics']:
        if i.link == '/physics/atomic-structure':
            return render_template('atomic-structure.html', card=i)
    return '404 error'


@app.route('/physics/atomic-structure/test', methods=['GET', 'POST'])
def test_atomic_structure():
    try:
        form = TestAtom()
        if current_user.id:
            if form.validate_on_submit():
                res = check_test(form, current_user.id, "Строение атома")
                return render_template('something_wrong.html', text='Данные успешно сохранены')
            return render_template('tests.html', form=form, title='Физика', link='physics', link2='atomic-structure')
    except Exception:
        return redirect("/enter_please")


@app.route('/physics/elec')
def elec_lesson():
    for i in CARDS['physics']:
        if i.link == '/physics/elec':
            return render_template('elec.html', card=i)
    return '404 error'


@app.route('/physics/elec/test', methods=['POST', 'GET'])
def test_elec():
    try:
        form = TestElec()
        if current_user.id:
            if form.validate_on_submit():
                res = check_test(form, current_user.id, "Электромагнитные волны")
                return render_template('something_wrong.html', text='Данные успешно сохранены')
            return render_template('tests.html', form=form, title='Физика', link='physics', link2='elec')
    except Exception:
        return redirect("/enter_please")


@app.route('/computers/binary')
def binary_lesson():
    for i in CARDS['computers']:
        if i.link == '/computers/binary':
            return render_template('binary.html', card=i)
    return '404 error'


@app.route('/computers/binary/test', methods=['POST', 'GET'])
def test_binary():
    try:
        form = TestBinary()
        if current_user.id:
            if form.validate_on_submit():
                res = check_test(form, current_user.id, "Двоичная система")
                return render_template('something_wrong.html', text='Данные успешно сохранены')
            return render_template('tests.html', form=form, title='Информатика', link='computers', link2='binary')
    except Exception:
        return redirect("/enter_please")


@app.route('/computers/cpu')
def cpu_lesson():
    for i in CARDS['computers']:
        if i.link == '/computers/cpu':
            return render_template('cpu.html', card=i)
    return '404 error'


@app.route('/computers/cpu/test', methods=['POST', 'GET'])
def test_cpu():
    try:
        form = TestCPU()
        if current_user.id:
            if form.validate_on_submit():
                res = check_test(form, current_user.id, "Процессор")
                return render_template('something_wrong.html', text='Данные успешно сохранены')
            return render_template('tests.html', form=form, title='Информатика', link='computers', link2='cpu')
    except Exception:
        return redirect("/enter_please")


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


@app.route('/test-had-been-passed')
def test_passed():
    # если тест был пройден
    return render_template('something_wrong.html', text='Тест уже был пройден')


@app.route("/profile")
def profile():
    cards = []
    result = []
    db_sess = create_session()
    for i in CARDS.keys():
        for j in CARDS[i]:
            cards.append(j)
            req = list(db_sess.query(Result).filter(Result.lesson_name == j.name))
            if len(req) > 0:
                result.append(str(req[-1].percent))
            else:
                result.append("не пройдено")
    return render_template('profile.html', title=f'{current_user.name} {current_user.surname}',
                           result=result,
                           cards=cards)


def check_test(form, user_id, name):
    count = 0
    for i, j in enumerate(form):
        if len(form.answers) > i:
            if j.data == form.answers[i]:
                count += 1
        else:
            break
    res = f"{count}/{len(form.answers)}"
    db_sess = create_session()
    result = Result()
    result.user_id = user_id
    result.lesson_name = name
    result.percent = res
    db_sess.add(result)
    db_sess.commit()
    return res


if __name__ == '__main__':
    global_init("db/project.db")
    app.run(debug=True)
