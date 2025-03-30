from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError, Email
from wtforms import StringField, PasswordField, SubmitField


class LoginForm(FlaskForm):
    email = StringField('Почта', validators=[
                        DataRequired(), Email(message='Введите почту корректно')])
    password = PasswordField("Пароль", validators=[
                             DataRequired(), Length(min=6, max=30)])
    submit = SubmitField("Войти")
