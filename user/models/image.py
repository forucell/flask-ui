from user.extensions import db, upload_set


class Image(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    filename = db.Column(db.String(128), unique=True)

    member_id = db.Column(db.Integer, db.ForeignKey('member.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


    # __table_args__ = (db.UniqueConstraint('user_id', 'name', name='unique_name_user_id'),)

    # users = db.relationship('User', secondary='user_image')

    @property
    def url(self):
        return upload_set.url(self.filename)

    @property
    def filepath(self):
        if self.filename is None:
            return
        return upload_set.path(self.filename)



    def __repr__(self):
        return (self.id)

    # def __str__(self):
    #     return f'{self.name}'
