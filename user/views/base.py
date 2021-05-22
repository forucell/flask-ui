from flask_admin.contrib.sqla import ModelView
from flask import redirect, url_for
from flask_user import current_user

from user.utils import has_role

class BaseView(ModelView):
    __abstract__ = True

    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('user.login', next='/admin'))

    # def is_visible(self):
    #     role = 'agent'
    #     if has_role(role):
    #         return False
    #     return True