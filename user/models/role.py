from user.extensions import db

# Define the Role data-model
class Role(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)

    def __str__(self):
        return self.name

    # def __repr__(self):
    #     return self.name