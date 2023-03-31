




from flask import Flask
from .extensions import db
from .route import shortener

def create_app(config_file='settings.py'):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    db.init_app(app)
    app.register_blueprint(shortener)
    from . import model
    with app.app_context():
        db.create_all()
    return app
