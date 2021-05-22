from flask import Flask

from user.extensions import db, admin, upload_set

from flask_user import UserManager

from user.config import ConfigClass
from user.rest import routes

from user.models import User, Role, UserRole, Image, Comment, Member
from user.views import UserView, RoleView, UserRoleView, ImageView, CommentView, MemberView

from datetime import datetime

from flask_uploads import configure_uploads, patch_request_class

from flask_babelex import Babel

app = Flask(__name__)

def create_app():
    """Application factory, used to create application
    """
    configure_app(app)
    configure_extensions(app)
    user_manager = UserManager(app, db, User)
    # configure_user_manager(app)
    create_db(app, user_manager)
    # insert_into(app, user_manager)
    register_views(app)
    register_blueprints(app)
    return app


def configure_app(app):
    app.config.from_object(ConfigClass)


def configure_extensions(app):
    db.init_app(app)
    admin.init_app(app)

    configure_uploads(app, upload_set)
    patch_request_class(app, 16 * 1024 * 1024)

def register_views(app):
    # admin.add_view(UserView(User, db.session, menu_icon_type='glyph', menu_icon_value='glyphicon-home'))
    admin.add_view(UserView(User, db.session))
    admin.add_view(RoleView(Role, db.session))
    admin.add_view(UserRoleView(UserRole, db.session))
    admin.add_view(ImageView(Image, db.session))
    # admin.add_view(CommentView(Comment, db.session))
    admin.add_view(MemberView(Member, db.session))


def register_blueprints(app):
    app.register_blueprint(routes.blueprint)


# def configure_user_manager(app):
#     from user.models import User
#     return UserManager(app, db, User)

#














def create_db(app, user_manager):
    with app.app_context():
        db.create_all()
        db.session.commit()



def insert_into(app, user_manager):
    with app.app_context():
        # db.create_all()

        # Create 'member@example.com' user with no roles
        if not User.query.filter(User.email == 'member@example.com').first():
            user = User(
                email='user@example.com',
                username='user',
                email_confirmed_at=datetime.utcnow(),
                password=user_manager.hash_password('Test1234'),
            )

            user.roles.append(Role(name='user'))

            db.session.add(user)
            db.session.commit()

        # Create 'member@example.com' user with no roles
        if not User.query.filter(User.email == 'member@example.com').first():
            user = User(
                email='agent@example.com',
                username='agent',
                email_confirmed_at=datetime.utcnow(),
                password=user_manager.hash_password('Test1234'),
            )

            user.roles.append(Role(name='agent'))

            db.session.add(user)
            db.session.commit()

        # Create 'admin@example.com' user with 'Admin' and 'Agent' roles
        if not User.query.filter(User.email == 'admin@example.com').first():
            user = User(
                email='admin@example.com',
                username='admin',
                email_confirmed_at=datetime.utcnow(),
                password=user_manager.hash_password('Test1234'),
            )
            user.roles.append(Role(name='admin'))
            db.session.add(user)
            db.session.commit()