from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = 'kwez.db'  # SQLite database name

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "JANURR"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:bajentingjanurrpogi123@127.0.0.1:3306/kwez'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    
    from .auth import auth as auth_blueprint
    from .views import views as views_blueprint

    app.register_blueprint(auth_blueprint, url_prefix='/')
    app.register_blueprint(views_blueprint, url_prefix='/')
    
    from .models import Users, Scores
    
    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Create database!')
