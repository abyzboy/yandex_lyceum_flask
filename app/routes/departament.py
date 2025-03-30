from flask import Blueprint, render_template, redirect, url_for, flash
from database.db_session import create_session
from models.all_models import Department, User
from flask_login import current_user, login_required
from forms.department import CreateDepartmentForm, RedactDepartmentForm
from services import add_members
from datetime import datetime
department_bp = Blueprint('department', __name__)


@department_bp.route('/departments/show')
def show():
    db_ses = create_session()
    departments = db_ses.query(Department).all()
    return render_template('show_departments.html', departments=departments)


@login_required
@department_bp.route('/departments/add', methods=['GET', 'POST'])
def create():
    form = CreateDepartmentForm()
    if form.validate_on_submit():
        db_ses = create_session()
        members = list(
            map(int, form.members.data.replace(',', ' ').split()))
        cheif = db_ses.query(User).get(current_user.id)
        department = Department(title=form.title.data,
                                email=form.email.data, chief=cheif)
        if members:
            for member in members:
                add_members(db_ses, department, member)
        db_ses.add(department)
        db_ses.commit()
        return redirect(url_for('department.show'))
    return render_template('create_department.html', form=form)


@login_required
@department_bp.route('/departments/redact/<int:department_id>', methods=['GET', 'POST'])
def redact(department_id):
    form = RedactDepartmentForm()
    if form.validate_on_submit():
        db_ses = create_session()
        department = db_ses.query(Department).filter(
            Department.id == department_id).first()
        if department.chief_id == current_user.id or current_user.id == 1:
            members = list(
                map(int, form.members.data.replace(',', ' ').split()))
            if members:
                department.members.clear()
                for member in members:
                    add_members(db_ses, department, member)
            department.title = form.title.data
            department.email = form.email.data
            db_ses.commit()
            return redirect(url_for('department.show'))
        else:
            flash('Вы не можете редактировать данную работу', 'danger')
    return render_template('redact_department.html', form=form, department_id=department_id)


@login_required
@department_bp.route('/departments/delete/<int:department_id>', methods=['GET', 'POST'])
def delete(department_id):
    db_ses = create_session()
    department = db_ses.query(Department).filter(
        Department.id == department_id).first()
    if department and current_user.id == 1 or current_user.id == department.chief_id:
        db_ses.refresh(department)
        db_ses.delete(department)
        db_ses.commit()
        db_ses.close()
        flash('Работа удалена', 'success')
    return redirect(url_for('department.show'))
