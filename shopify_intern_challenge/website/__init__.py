from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path, system
from flask_login import LoginManager


#INITIALIZE THE DATABASE NAME
db = SQLAlchemy()
DB_NAME = "database.db"





'''
-Create the flask app and import the modules needed 
-views and auth kept separate 
-Initialize login manager object
-Load the current User if still logged in'''
def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"]= "#W8NFB2gWpX6EHEp"
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

