from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path, system
from flask_login import LoginManager



db = SQLAlchemy()
DB_NAME = "database.db"


extensions_allowed = ["png", "gif", "jpg", "jpeg"]
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in extensions_allowed





def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"]= "#nfnt2030"

    # configure the database for the repository
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views 
    from .auth import auth

    app.register_blueprint(views, url_prefix = "/")
    app.register_blueprint(auth, url_prefix = "/")
    
    from .models import User, Note, Img
    create_database(app)
    
    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)


    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    return app







def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print("Database Created")

