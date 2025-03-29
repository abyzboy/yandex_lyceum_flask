from flask import Flask
from database import db_session
from models.all_models import *
from routes.main import main_bp

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init('app\mars_explorer.sqlite')
    app.register_blueprint(main_bp)
    app.run(debug=True)


if __name__ == '__main__':
    main()
