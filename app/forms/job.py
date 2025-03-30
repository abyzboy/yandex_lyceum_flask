from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError, Email
from wtforms import StringField, PasswordField, SubmitField, IntegerField


class CreateJobForm(FlaskForm):
    job = StringField('Работа', validators=[
        DataRequired()])
    worksize = IntegerField("Время работы", validators=[
        DataRequired()])
    collabarators = StringField('Помошники')
    submit = SubmitField("Создать")
