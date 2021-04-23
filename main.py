from datetime import datetime
from flask import Flask, request, render_template
from data.db_session import create_session, global_init
from data.users import User

from forms import *
from cards import *

app = Flask(__name__)
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


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if request.method == 'GET':
        return render_template('login.html', form=form)
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
    form = SequencesTest()
    if form.validate_on_submit():
        return 'Данные успешно сохранены'
    return render_template('test_sequences.html', form=form)


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
    form = TestStereometry()
    if form.validate_on_submit():
        return 'Данные успешно сохранены'
    return render_template('test_stereometry.html', form=form)


@app.route('/physics/atomic-structure')
def atomic_structure_lesson():
    for i in CARDS['physics']:
        if i.link == '/physics/atomic-structure':
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
            return render_template('elec.html', card=i)
    return '404 error'


@app.route('/physics/elec/test', methods=['POST', 'GET'])
def test_elec():
    form = TestElec()
    if form.validate_on_submit():
        return "Данные успешно сохранены"
    return render_template('test_elec.html', form=form)


@app.route('/computers/binary')
def binary_lesson():
    for i in CARDS['computers']:
        if i.link == '/computers/binary':
            return render_template('binary.html', card=i)
    return '404 error'


@app.route('/computers/binary/test', methods=['POST', 'GET'])
def test_binary():
    form = TestBinary()
    if form.validate_on_submit():
        return 'Данные успешно сохранены'
    return render_template('test_binary.html', form=form)


@app.route('/computers/cpu')
def cpu_lesson():
    for i in CARDS['computers']:
        if i.link == '/computers/cpu':
            return render_template('cpu.html', card=i)
    return '404 error'


@app.route('/computers/cpu/test', methods=['POST', 'GET'])
def test_cpu():
    form = TestCPU()
    if form.validate_on_submit():
        return 'Данные успешно сохранены'
    return render_template('test_cpu.html', form=form)


@app.route("/registration", methods=['POST', 'GET'])
def registration():
    form = RegisterForm()
    if request.method == 'GET':
        return render_template('registration.html', title='Регистрация', form=form)
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


@app.route("/profile/<int:user_id>")
def profile(user_id):
    print(request.user_id)


if __name__ == '__main__':
    app.run(debug=True)
