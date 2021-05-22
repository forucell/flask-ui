from user.extensions import db
from flask_login import UserMixin


class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20))
    password = db.Column(db.String(50))

    # images = db.relationship('Image', secondary='user_image')

    images = db.relationship('Image', backref='member', lazy='dynamic')

    def __repr__(self):
        return '<Member %r>' % self.username


