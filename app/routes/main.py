from flask import Blueprint, render_template
from database.db_session import create_session
from models.all_models import Jobs
from flask_login import current_user
main_bp = Blueprint('main', __name__)


@main_bp.route('/', methods=['GET'])
def home():
    db_ses = create_session()
    jobs = db_ses.query(Jobs).all()
    return render_template('index.html', jobs=jobs)
