from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth
from flask_login import LoginManager
from werkzeug.security import generate_password_hash
from flask_bcrypt import Bcrypt
from flaskblog.config import Config



db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.admin'
login_manager.login_message_category = 'info'
http_auth = HTTPBasicAuth()



users = {
    "admin": generate_password_hash("blogpass123"),
}







def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {"pool_pre_ping": True}  

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    from flaskblog.users.routes import users
    from flaskblog.posts.routes import posts
    from flaskblog.main.routes import main
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    
    return app