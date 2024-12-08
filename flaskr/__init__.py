from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
class Base(DeclarativeBase):
    pass
db=SQLAlchemy(model_class=Base)
csrf=CSRFProtect()
def create_app():
    app=Flask(__name__,instance_relative_config=True)
    #configure instance
    app.config.from_pyfile("config.py",silent=True)
    #csrf protection
    csrf.init_app(app)
    
    #database connection
    app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root@localhost/student'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
    db.init_app(app)
    #You need to import all models here.
    import flaskr.models
    with app.app_context():
        db.create_all()
    #for registering blueprint
    from flaskr import index
    app.register_blueprint(index.bp)
    return app