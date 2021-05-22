from flask import flash, render_template
from datetime import datetime

from flask import Flask, render_template_string
from flask_sqlalchemy import SQLAlchemy
from flask_user import UserManager, UserMixin, login_required, roles_required
# from flask_babelex import Babel

from .config import ConfigClass

def create_app():
    """ Flask application factory """

    # Create Flask app load app.config
    app = Flask(__name__)
    # app.config.from_object(__name__ + '.ConfigClass')

    app.config.from_object(ConfigClass)

    # # Initialize Flask-BabelEx
    # babel = Babel(app)

    # Initialize Flask-SQLAlchemy
    db = SQLAlchemy(app)

    @app.route('/')
    def home_page():
        flash('Message sent successfully', 'success')
        flash("This page is restricted. Please enter as an admin", 'error')

        return render_template("about.html")

    return app


