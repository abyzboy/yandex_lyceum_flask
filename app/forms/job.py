from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError, Email
from wtforms import StringField, PasswordField, SubmitField, IntegerField, BooleanField


class CreateJobForm(FlaskForm):
    job = StringField('Работа', validators=[
        DataRequired()])
    worksize = IntegerField("Время работы", validators=[
        DataRequired()])
    collabarators = StringField('Помошники')
    submit = SubmitField("Создать")


class RedactJobForm(FlaskForm):
    job = StringField('Работа', validators=[
        DataRequired()])
    worksize = IntegerField("Время работы", validators=[
        DataRequired()])
    collabarators = StringField('Помошники')
    is_finished = BooleanField('Завершить работу')
    submit = SubmitField("Создать")
