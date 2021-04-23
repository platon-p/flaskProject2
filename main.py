from datetime import datetime
from flask import Flask, request, render_template
from data.db_session import create_session, global_init
from data.users import User

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, RadioField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


class MainCards:
    def __init__(self, img, name, link):
        self.img, self.name, self.link = img, name, link
        self.lenght = len(CARDS[self.link])


@app.route('/')
def hello_world():
    cards = [MainCards('shapes.svg', 'Математика', 'math'), MainCards('magnet.svg', 'Физика', 'physics'),
             MainCards('computer.svg', 'Информатика', 'computers')]
    return render_template('ind.html', title='Моя школа', cards=cards)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


class LoginForm(FlaskForm):
    mail = StringField(validators=[DataRequired()],
                       render_kw={'class': 'user-input mail_input_field', 'placeholder': 'Почта'})
    password = PasswordField(validators=[DataRequired()],
                             render_kw={'class': 'passw_input password-input-field', 'placeholder': 'Пароль'})
    submit = SubmitField('Войти', render_kw={'class': 'log_in_btn', 'style': 'width: 15em'})


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


class CardOfLesson:
    def __init__(self, color, source, link, name):
        self.color, self.source, self.link, self.name = color, source, link, name


CARDS = {'math': (
    CardOfLesson('#DC8754', '123-numbers.svg', '/math/sequences',
                 'Последовательности'),
    CardOfLesson('#A858D6', 'cone.svg', '/math/stereometry', 'Стереометрия')),
    'physics': (
        CardOfLesson('#EB6A7D', 'wave.svg', '/physics/elec',
                     'Электромагнитные волны'),
        CardOfLesson('#00A8AB', 'atom.svg', '/physics/atomic-structure',
                     'Строение атома')),
    'computers': (CardOfLesson('#71D780', 'binary.svg', '/computers/binary',
                               'Двоичная система'),
                  CardOfLesson('#5660FF', 'processor.svg', '/computers/cpu', 'Процессор'))
}


@app.route('/math')
def math_lesson():
    cards = CARDS['math']
    return render_template('lesson.html', title='Математика', cards=cards)


@app.route('/math/sequences')
def sequences_lesson():
    for i in CARDS['math']:
        if i.link == '/math/sequences':
            return render_template('sequences.html', card=i)
    return '404 error'


@app.route('/math/stereometry')
def stereometry_lesson():
    for i in CARDS['math']:
        if i.link == '/math/stereometry':
            return render_template('stereometry.html', card=i)
    return '404 error'


@app.route('/physics')
def ph_lesson():
    cards = CARDS['physics']
    return render_template('lesson.html', title='Физика', cards=cards)


@app.route('/physics/atomic-structure')
def atomic_structure_lesыon():
    for i in CARDS['physics']:
        if i.link == '/physics/atomic-structure':
            return render_template('atomic-structure.html', card=i)
    return '404 error'


class AtomTest(FlaskForm):
    q1 = RadioField(label='1.К субатомным частицам не относится:', choices=['Протон', 'Нейтрон', 'Электрон', 'Фотон'],
                    render_kw={'class': 'radio-label'})
    q2 = '2.Порядковый номер в таблице Менделеева соответствует:'

    bool1, bool2, bool3, bool4 = BooleanField('Массе атома'), BooleanField(
        'Количеству протонов/электронов'), BooleanField('Заряду ядра'), BooleanField(
        'Количество электронов на внешнем уровне')
    q3 = StringField(label='3.Планетарную модель атома разработал:',
                     render_kw={'class': 'mail_input_field', 'placeholder': 'Фамилия изобретателя',
                                'style': 'line-height: 2em'})
    q4 = RadioField(label='4. Тритий - это изотоп:', choices=['Кислорода', 'Водорода', 'Гелия', 'Свинца'],
                    render_kw={'class': 'radio-label'})
    submit = SubmitField('Отправить', render_kw={'class': 'log_in_btn'})
    answers = ('Фотон', 'False', 'True', 'True', 'False', 'Резерфорд', 'Водорода')


@app.route('/physics/atomic-structure/test', methods=['GET', 'POST'])
def test_atomic_structure():
    form = AtomTest()
    if request.method == 'GET':
        return render_template('tests-atomic-structure.html', form=form)
    else:
        return 'Данные успешно сохранены'


@app.route('/physics/elec')
def elec_lesson():
    for i in CARDS['physics']:
        if i.link == '/physics/elec':
            return render_template('elec.html', card=i)
    return '404 error'


class TestElec(FlaskForm):
    q1 = RadioField(label='1.Согласно теории Максвелла электромагнитные волны излучаются:',
                    choices=('только при равномерном движении электронов по прямой',
                             'только при гармонических колебаниях заряда',
                             'только при равномерном движении заряда по окружности',
                             'при любом неравномерном движении заряда'),
                    render_kw={'class': 'radio-label'})
    q2 = RadioField(label='2.Заряженная частица излучает электромагнитные волны:',
                    choices=('только при движении с ускорением',
                             'только при движении с постоянной скоростью',
                             'только в состоянии покоя',
                             'как в состоянии покоя, так и при движении с постоянной скоростью'),
                    render_kw={'class': 'radio-label'})
    q3 = RadioField(label='3.Заряженная частица не излучает электромагнитные волны при:',
                    choices=('равномерном прямолинейном движении',
                             'равномерном движении по окружности',
                             'колебательном движении',
                             'любом движении с ускорением'),
                    render_kw={'class': 'radio-label'})
    q4 = RadioField(
        label='4. Какое из приведенных ниже природных явлений не может служить примером излучения электромагнитных '
              'волн?',
        choices=('Молния', 'Полярное сияние', 'Излучение звезд', 'Гром'),
        render_kw={'class': 'radio-label'})
    submit = SubmitField('Отправить', render_kw={'class': 'log_in_btn'})


@app.route('/physics/elec/test', methods=['POST', 'GET'])
def test_elec():
    form = TestElec()
    if request.method == 'GET':
        return render_template('test_elec.html', form=form)
    elif request.method == 'POST':
        return "Данные успешно сохранены"


@app.route('/computers')
def inf_lesson():
    cards = CARDS['computers']
    return render_template('lesson.html', title='Информатика', cards=cards)


@app.route('/computers/binary')
def binary_lesson():
    for i in CARDS['computers']:
        if i.link == '/computers/binary':
            return render_template('binary.html', card=i)
    return '404 error'


@app.route('/computers/cpu')
def cpu_lesson():
    for i in CARDS['computers']:
        if i.link == '/computers/cpu':
            return render_template('cpu.html', card=i)
    return '404 error'


class RegisterForm(FlaskForm):
    surname = StringField(render_kw={'class': 'user-input mail_input_field', 'placeholder': 'Фамилия'})
    name = StringField(render_kw={'class': 'user-input mail_input_field', 'placeholder': 'Имя'})
    mail = StringField(render_kw={'class': 'user-input mail_input_field necessarily', 'placeholder': 'Почта'})
    password = PasswordField(render_kw={'class': 'user-input mail_input_field necessarily', 'placeholder': 'Пароль'})
    submit = SubmitField('Регистрация', render_kw={'class': 'log_in_btn', 'style': 'width: 15em'})


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
def profile():
    print(request.user_id)


if __name__ == '__main__':
    app.run(debug=True)
