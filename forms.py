from wtforms import StringField, PasswordField, BooleanField, SubmitField, RadioField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    mail = StringField(validators=[DataRequired()],
                       render_kw={'class': 'user-input mail_input_field', 'placeholder': 'Почта'})
    password = PasswordField(validators=[DataRequired()],
                             render_kw={'class': 'passw_input password-input-field', 'placeholder': 'Пароль'})
    submit = SubmitField('Войти', render_kw={'class': 'log_in_btn', 'style': 'width: 15em'})


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
    surname = StringField(render_kw={'class': 'user-input mail_input_field', 'placeholder': 'Фамилия'})
    name = StringField(render_kw={'class': 'user-input mail_input_field', 'placeholder': 'Имя'})
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


class SequencesTest(FlaskForm):
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
