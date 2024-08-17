from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__) # root path
    app.config['SECRET_KEY'] = "jiofepwaj fioepwjfiopwea" # Flask signs session cookies with this
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_NAME}"
    db.init_app(app) # for database to work with flask app

    # below: import blueprint objects from views and auth modules -- 
        # organizes application into smaller components
    from .views import views
    from .auth import auth

    # register blueprints with flask app
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    # imports the models that define the structure of the tables in the db
    from .models import User, Note

    with app.app_context(): #db operations can be performed
        db.create_all() # creates the tables defined in models

    login_manager = LoginManager() # handles user sessions and authentications
    login_manager.login_view = "auth.login" # security measure if user tries to access without logged in, they will be redirected to this
    login_manager.init_app(app) # initializes login manager with flask app

    @login_manager.user_loader # use this decorator to load user
    def load_user(id):
        return User.query.get(int(id)) # it will look for primary key of user and return user object

    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME): # if the db doesn't already exist,
      db.create_all(app=app) #creates db
      print("Created Database!")