import os

from flask import Flask, render_template
from app.models import db


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=os.environ.get
        ("SECRET_KEY")
    )
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///base.db'

    #db.init_app(app)

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)

    else:
        app.config.from_mapping(test_config)

    @app.route('/')
    def hello():
        return render_template("index.html")

    @app.route('/card')
    def card():
        return render_template("card.html")

    @app.route('/create')
    def create_card():
        return render_template("create.html")

    @app.route('/change')
    def change_card():
        return render_template("change.html")

    return app
