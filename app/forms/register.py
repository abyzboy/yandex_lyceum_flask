from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError, EqualTo, Email, Length
from models.all_models import User
from database.db_session import create_session


class RegistrationForm(FlaskForm):
    surname = StringField(
        "ФАМИЛИЯ", validators=[DataRequired(), Length(min=2, max=80)])
    name = StringField(
        "ИМЯ", validators=[DataRequired(), Length(min=2, max=80)])
    email = StringField('Почта', validators=[
                        DataRequired(), Email(message='Введите почту корректно')])
    password = PasswordField("Пароль", validators=[
                             DataRequired(), Length(min=6, max=30)])
    confirm_password = PasswordField("Подтвердите пароль", validators=[
                                     DataRequired(), EqualTo('password')])
    submit = SubmitField("Зарегистрироваться")

    def validate_email(self, email):
        user = create_session().query(User).filter_by(email=email.data).first()
        if user:
            raise ValidationError(
                "Данная почта уже занята. Пожалуйста, выберите другое...")
