from user.extensions import db
from flask_user import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    active = db.Column('is_active', db.Boolean(), nullable=False, server_default='1')

    # User authentication information. The collation='NOCASE' is required
    # to search case insensitively when USER_IFIND_MODE is 'nocase_collation'.
    email = db.Column(db.String(255, collation='NOCASE'), nullable=False, unique=True)
    email_confirmed_at = db.Column(db.DateTime())
    password = db.Column(db.String(255), nullable=False, server_default='')

    # User information
    first_name = db.Column(db.String(100, collation='NOCASE'), nullable=False, server_default='')
    last_name = db.Column(db.String(100, collation='NOCASE'), nullable=False, server_default='')

    # Define the relationship to Role via UserRoles
    roles = db.relationship('Role', secondary='user_role')

    images = db.relationship('Image', backref='user', lazy='dynamic')

    # def __str__(self):
    #     return self.username

    # def __repr__(self):
    #     return self.username

    def __repr__(self):
        return '<User %r>' % self.username


# from user.app import app
# from user.extensions import login_manager
# login_manager.init_app(app)
#
# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(user_id)


