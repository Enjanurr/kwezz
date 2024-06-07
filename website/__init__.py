from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = 'kwez.db'  # SQLite database name

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "JANURR"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://root:bajentingjanurrpogi123@127.0.0.1:3306/{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    from .models import Users, Scores
    
    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Create database!')
