from flask import Blueprint, render_template, redirect, url_for
from database.db_session import create_session
from models.all_models import User
from forms.register import RegistrationForm
from forms.login import LoginForm
from flask_login import login_user, current_user
from database.db_session import create_session
from extensions import bcrypt

user_bp = Blueprint('user', __name__)


@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        db_ses = create_session()
        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        user = User(name=form.name.data, surname=form.surname.data,
                    hashed_password=hashed_password, email=form.email.data)
        db_ses.add(user)
        db_ses.commit()
        login_user(user)
        return redirect(url_for('main.home'))
    return render_template('registration.html', form=form)


@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        ...
    return render_template('login.html', form=form)
