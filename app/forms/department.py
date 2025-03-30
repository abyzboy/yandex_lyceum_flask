from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField, SubmitField, EmailField


class CreateDepartmentForm(FlaskForm):
    title = StringField('Название', validators=[
        DataRequired()])
    email = StringField("Почта", validators=[
        DataRequired()])
    members = StringField('Помошники')
    submit = SubmitField("Создать")


class RedactDepartmentForm(FlaskForm):
    title = StringField('Название', validators=[
        DataRequired()])
    email = EmailField("Почта", validators=[
        DataRequired()])
    members = StringField('Помошники')
    submit = SubmitField("Изменить")
