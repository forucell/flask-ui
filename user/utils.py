from user.models import User

from flask_user import current_user

def has_role(role):
    user = User.query.filter_by(id=current_user.id).filter(User.roles.any(name=role)).first()
    if user:
        return True
    return False
