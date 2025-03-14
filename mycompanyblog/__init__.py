import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


app = Flask(__name__)


basedir = os.path.abspath(os.path.dirname(__name__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config["SECRET_KEY"] = 'mysecretkey'

db = SQLAlchemy(app)
Migrate(app,db)


login_manager = LoginManager()

login_manager.init_app(app)
login_manager.login_view = 'user.login'


from mycompanyblog.core.views import core
from mycompanyblog.users.views import users
from mycompanyblog.blog_posts.views import blog_posts
from mycompanyblog.error_pages.handlers import error_pages
app.register_blueprint(core)
app.register_blueprint(users)
app.register_blueprint(blog_posts)
app.register_blueprint(error_pages)

