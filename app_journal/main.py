from flask import Flask
from database import db_session
from services import add_job, add_collaborator, add_user
from models.all_models import *
from routes.main import main_bp
from datetime import datetime

app = Flask(__name__)
db_session.global_init('app\\mars_explorer.sqlite')
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    app.register_blueprint(main_bp)
    app.run(debug=True)


if __name__ == '__main__':
    main()
