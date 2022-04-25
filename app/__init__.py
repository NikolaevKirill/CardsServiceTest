import os

from flask import Flask

from .models import db
from .routes import main


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=os.environ.get
        ("SECRET_KEY")
    )
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///base.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.register_blueprint(main)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)

    else:
        app.config.from_mapping(test_config)

    return app
