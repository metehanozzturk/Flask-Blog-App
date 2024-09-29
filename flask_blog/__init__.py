import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_blog.config import Config

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login' #to not let users get to pages without loging in
login_manager.login_message_category = 'info' #bootstrap category for better info message
mail = Mail()
print(os.environ.get("EMAIL_USER"))



def create_app(config_class=Config):
        app = Flask(__name__)
        app.config.from_object(Config)

        db.init_app(app)
        bcrypt.init_app(app)
        login_manager.init_app(app)
        mail.init_app(app)

        from flask_blog.users.routes import users
        from flask_blog.posts.routes import posts
        from flask_blog.main.routes import main
        from flask_blog.errors.handlers import errors

        app.register_blueprint(users)
        app.register_blueprint(posts)
        app.register_blueprint(main)
        app.register_blueprint(errors)


        with app.app_context():
                db.create_all()  # This creates the database file and tables if they don't exist

        print(os.environ.get("EMAIL_USER"))
        return app