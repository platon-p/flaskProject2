from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, RadioField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    email = EmailField(validators=[DataRequired()],
                       render_kw={'class': 'user-input mail_input_field', 'placeholder': 'Почта'})
    password = PasswordField(validators=[DataRequired()],
                             render_kw={'class': 'passw_input password-input-field', 'placeholder': 'Пароль'})
    submit = SubmitField('Войти', render_kw={'class': 'log_in_btn', 'style': 'width: 15em'})


class TestAtom(FlaskForm):
    q1 = RadioField(label='1.К субатомным частицам не относится:', choices=['Протон', 'Нейтрон', 'Электрон', 'Фотон'],
                    render_kw={'class': 'radio-label'})
    q2 = RadioField('2.Порядковый номер в таблице Менделеева соответствует:',
                    choices=('Количеству протонов/электронов', 'Массе атома',
                             'Количеству электронов на внешнем уровне', 'Номеру группы'),
                    render_kw={'class': 'radio-label'})

    q3 = StringField(label='3.Планетарную модель атома разработал:',
                     render_kw={'class': 'mail_input_field', 'placeholder': 'Фамилия изобретателя',
                                'style': 'line-height: 2em'})
    q4 = RadioField(label='4. Тритий - это изотоп:', choices=['Кислорода', 'Водорода', 'Гелия', 'Свинца'],
                    render_kw={'class': 'radio-label'})
    submit = SubmitField('Отправить', render_kw={'class': 'log_in_btn'})
    answers = ('Фотон', 'Количеству протонов/электронов', 'Резерфорд', 'Водорода')


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


class RegisterForm(FlaskForm):
    surname = StringField(validators=[DataRequired()],
                          render_kw={'class': 'user-input mail_input_field necessarily', 'placeholder': 'Фамилия'})
    name = StringField(validators=[DataRequired()],
                       render_kw={'class': 'user-input mail_input_field necessarily', 'placeholder': 'Имя'})
    mail = StringField(validators=[DataRequired()],
                       render_kw={'class': 'user-input mail_input_field necessarily', 'placeholder': 'Почта'})
    password = PasswordField(validators=[DataRequired()],
                             render_kw={'class': 'user-input mail_input_field necessarily', 'placeholder': 'Пароль'})
    submit = SubmitField('Регистрация', render_kw={'class': 'log_in_btn', 'style': 'width: 15em'})


class TestBinary(FlaskForm):
    q1 = RadioField('Какому числу в двоичной системе соответствует число 45 ?',
                    choices=('101101', '101010', '110111', '100010'), render_kw={'class': 'radio-label'})
    q2 = RadioField('Какому числу в двоичной системе соответствует число 107 ?',
                    choices=('1010111', '1001010', '1101011', '1000101'), render_kw={'class': 'radio-label'})
    q3 = RadioField('Какому числу в десятичной системе соответствует число 1000001 ?',
                    choices=('33', '58', '45', '65'), render_kw={'class': 'radio-label'})
    q4 = RadioField('Какому числу в двоичной системе соответствует число 11100111 ?',
                    choices=('184', '199', '231', '291'), render_kw={'class': 'radio-label'})
    submit = SubmitField('Отправить', render_kw={'class': 'log_in_btn'})
    answers = ('101101', '1101011', '65', '231')


class TestSequences(FlaskForm):
    q1 = RadioField('Каким способом задана последовательность: "Последовательность простых чисел"',
                    choices=('Словесным', 'Рекуррентным', 'Формулой'), render_kw={'class': 'radio-label'})
    q2 = RadioField('Каким способом задана последовательность: "a_1=1; a_2=1, a_n = a_(n-1)+a_(n-2)"',
                    choices=('Словесным', 'Рекуррентным', 'Формулой'), render_kw={'class': 'radio-label'})
    q3 = RadioField('Каким способом задана последовательность: "a_n=1+2n"',
                    choices=('Словесным', 'Рекуррентным', 'Формулой'), render_kw={'class': 'radio-label'})
    q4 = RadioField('Каким способом задана последовательность: "a_n=7+0.3n"',
                    choices=('Словесным', 'Рекуррентным', 'Формулой'), render_kw={'class': 'radio-label'})
    submit = SubmitField('Отправить', render_kw={'class': 'log_in_btn'})
    answers = ('Словесным', 'Рекуррентным', 'Формулой', 'Формулой')


class TestCPU(FlaskForm):
    q1 = RadioField('Процессор могут обозначать как...',
                    choices=('GPU', 'CPU', 'AMD', 'ARM'), render_kw={'class': 'radio-label'})
    q2 = RadioField('Промежуток времени между двумя последовательными электрическими импульсами называется...',
                    choices=('Ядром', 'Видеокартой', 'Частотой', 'Тактом'), render_kw={'class': 'radio-label'})
    q3 = RadioField(
        'Максимальная длина двоичного кода, который может обрабатываться или передаваться одновременно, называется ...',
        choices=('Байтом', 'Разрядностью процессора', 'МГц', 'Архитектурой'), render_kw={'class': 'radio-label'})
    q4 = RadioField('1000 МГц соответствует...',
                    choices=('1КГц', '10ГГц', '1ГГц', '300КГц'), render_kw={'class': 'radio-label'})
    submit = SubmitField('Отправить', render_kw={'class': 'log_in_btn'})
    answers = ('CPU', 'Тактом', 'Разрядностью процессора', '1ГГц')


class TestStereometry(FlaskForm):
    q1 = RadioField('Раздел геометрии, в котором изучают свойства фигур называется...',
                    choices=('Тригонометрия', 'Планиметрия', 'Стереометрия'), render_kw={'class': 'radio-label'})
    q2 = RadioField('Многоугольники, из которых состоит многогранник, называются...',
                    choices=('Прямоугольниками', 'Квадратами', 'Треугольниками', 'Гранями'),
                    render_kw={'class': 'radio-label'})
    q3 = RadioField(
        'Верно ли, что Диагональ многогранника — это отрезок, который соединяет две вершины, принадлежащие одной грани',
        choices=('Верно', 'Неверно'), render_kw={'class': 'radio-label'})
    q4 = RadioField('Стороны граней называются..',
                    choices=('Вершинами', 'Углами', 'Ребрами'), render_kw={'class': 'radio-label'})
    submit = SubmitField('Отправить', render_kw={'class': 'log_in_btn'})
    answers = ('Стереометрия', 'Гранями', 'Неверно', 'Ребрами')
