from flask import Flask
from flask.helpers import url_for
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager, login_manager

db=SQLAlchemy()
DB_NAME="database.db"
# sflix.sqlite
def create_app():
    app=Flask(__name__,template_folder="templates")
    app.config['SECRET_KEY']="abcd"
    app.config['SQLALCHEMY_DATABASE_URI']=f'sqlite:///{DB_NAME}'
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/sflix'
    
    
#     app.config['SQLALCHEMY_BINDS'] = {
#         'sflix': 'sqlite:///sflix.sqlite'
# }

    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')
    
    from .models import User,Note 
    
    create_database(app)
    
    login_manager=LoginManager()
    login_manager.login_view='auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))


    return app

def create_database(app):
    if not path.exists('website/'+DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
