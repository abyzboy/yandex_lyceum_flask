from flask import Blueprint, render_template, redirect, url_for
from database.db_session import create_session
from models.all_models import Jobs
from flask_login import current_user, login_required
from forms.job import CreateJobForm
from services import add_job
from datetime import datetime
job_bp = Blueprint('job', __name__)


@login_required
@job_bp.route('/addjob', methods=['GET', 'POST'])
def create():
    form = CreateJobForm()
    if form.validate_on_submit():
        db_ses = create_session()
        collaborators = list(
            map(int, form.collabarators.data.replace(',', ' ').split()))
        print(collaborators)
        add_job(db_ses, current_user.id, form.job.data, form.worksize.data,
                collaborators, datetime.now(), is_finished=False)
        db_ses.commit()
        return redirect(url_for('main.home'))
    return render_template('create_job.html', form=form)
