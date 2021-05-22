from user.extensions import db
from flask_user import UserMixin

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comment_text = db.Column(db.String(200))
    member_id = db.Column(db.Integer, db.ForeignKey('member.id'))

    def __repr__(self):
        return '<Comment %r>' % (self.id)
