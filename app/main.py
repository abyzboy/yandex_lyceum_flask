from flask import Flask
from database import db_session
from models.all_models import *
from routes.main import main_bp
from routes.user import user_bp
from routes.job import job_bp
from extensions import login_manager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init('app\\mars_explorer.sqlite')
    app.register_blueprint(job_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(user_bp)
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'
    login_manager.login_message = "Вы не можете получить доступ к данной странице нужно сначало войти"
    app.run(debug=True)


if __name__ == '__main__':
    main()
