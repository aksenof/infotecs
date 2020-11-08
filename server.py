from algorithm import factorization
from flask import Flask, redirect, url_for, render_template, send_from_directory
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key'  # секретный ключ для конфигурации


class MyForm(FlaskForm):  # класс для формы с вводом числа и кнопкой "ОК"
    input_number = StringField("Enter your number:", validators=[DataRequired()])
    submit = SubmitField('OK')


@app.route('/favicon.ico')
def favicon():  # значок для сайта
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/')
def go_to_index():  # переадресация на index
    return redirect(url_for('index'))


@app.route('/index', methods=['GET', 'POST'])
def index():  # то, что происходит в index
    form = MyForm()
    if form.validate_on_submit():
        number = form.input_number.data
        return redirect(url_for('result', number=number))  # передача введенного числа в result
    return render_template('index.html', form=form)


@app.route('/result/<number>')
def result(number):  # результат будет здесь
    try:
        res = factorization(int(number))  # разложение числа на простые множители
    except ValueError:
        res = "error, wrong data type, use only <int>"  # исключение на случай, если тип данных не int
    return render_template('result.html', number=number, result=res)


if __name__ == "__main__":
    app.run()  # запуск приложения
