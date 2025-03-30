from flask import Blueprint, render_template, redirect, url_for, flash
from database.db_session import create_session
from models.all_models import Jobs
from flask_login import current_user, login_required
from forms.job import CreateJobForm, RedactJobForm
from services import add_job, add_collaborator
from datetime import datetime
job_bp = Blueprint('job', __name__)


@login_required
@job_bp.route('/jobs/add', methods=['GET', 'POST'])
def create():
    form = CreateJobForm()
    if form.validate_on_submit():
        db_ses = create_session()
        collaborators = list(
            map(int, form.collabarators.data.replace(',', ' ').split()))
        add_job(db_ses, current_user.id, form.job.data, form.worksize.data,
                collaborators, datetime.now(), is_finished=False)
        db_ses.commit()
        return redirect(url_for('main.home'))
    return render_template('create_job.html', form=form)


@login_required
@job_bp.route('/jobs/redact/<int:job_id>', methods=['GET', 'POST'])
def redact(job_id):
    form = RedactJobForm()
    if form.validate_on_submit():
        db_ses = create_session()
        job = db_ses.query(Jobs).filter(Jobs.id == job_id).first()
        if job.team_leader_id == current_user.id:
            collaborators = list(
                map(int, form.collabarators.data.replace(',', ' ').split()))
            if collaborators:
                job.collaborators.clear()
                for collaborator in collaborators:
                    add_collaborator(db_ses, job, collaborator)
            job.job = form.job.data
            job.work_size = form.job.data
            job.is_finished = form.is_finished.data
            db_ses.commit()
            return redirect(url_for('main.home'))
        else:
            flash('Вы не можете редактировать данную работу', 'danger')
    return render_template('redact_job.html', form=form, job_id=job_id)


@login_required
@job_bp.route('/jobs/delete/<int:job_id>', methods=['GET', 'POST'])
def delete(job_id):
    db_ses = create_session()
    job = db_ses.query(Jobs).filter(Jobs.id == job_id).first()
    if job and current_user.id == 1 or current_user.id == job.team_leader_id:
        db_ses.refresh(job)
        db_ses.delete(job)
        db_ses.commit()
        db_ses.close()
        flash('Работа удалена', 'success')
    return redirect(url_for('main.home'))
