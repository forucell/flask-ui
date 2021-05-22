from user.extensions import db

# Define the UserRoles association table
class UserImage(db.Model):
    __tablename__ = 'user_image'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id', ondelete='CASCADE'))
    image_id = db.Column(db.Integer(), db.ForeignKey('image.id', ondelete='CASCADE'))