from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

login_manager.login_view = 'login'

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///datasave.db"
    app.config["SECRET_KEY"] = "teste"

    db.init_app(app)
    login_manager.init_app(app)
    
    with app.app_context():
        from . import routes
        from . import models

        db.create_all()

    from .models import Dados_alunos
    @login_manager.user_loader
    def load_user(user_id):
        return Dados_alunos.query.get(int(user_id))

    return app
