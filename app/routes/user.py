from flask import Blueprint, render_template, redirect, url_for, flash
from database.db_session import create_session
from models.all_models import User
from forms.register import RegistrationForm
from forms.login import LoginForm
from flask_login import login_user, current_user, logout_user
from database.db_session import create_session
from extensions import bcrypt
from services import add_user
user_bp = Blueprint('user', __name__)


@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        db_ses = create_session()
        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        user = add_user(db_ses, surname=form.surname.data, name=form.name.data, age=form.age.data,
                        position=form.position.data, speciality=form.speciality.data, address=form.address.data, email=form.email.data, hashed_password=hashed_password)
        login_user(user)
        db_ses.close()
        return redirect(url_for('main.home'))
    return render_template('registration.html', form=form)


@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_ses = create_session()
        user = db_ses.query(User).filter(User.email == form.email.data).first()
        if user and bcrypt.check_password_hash(user.hashed_password, form.password.data):
            login_user(user)
            return redirect(url_for('main.home'))
        else:
            flash('Ошибка входа. Проверьте email или пароль', 'danger')

    return render_template('login.html', form=form)


@user_bp.route('/logout', methods=['GET'])
def logout():
    logout_user()
    return redirect(url_for('main.home'))
