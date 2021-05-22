from flask_admin import AdminIndexView
from flask_user import current_user

from flask import redirect, url_for, flash

from user.utils import has_role

class MyAdminView(AdminIndexView):

    role_enabled = False
    pass_enabled = False

    def is_accessible(self):
        if current_user.is_active and current_user.is_authenticated:
            self.pass_enabled = True

            if has_role('admin'):
                self.role_enabled = True

                return True
        return False

    def is_visible(self):
        return False

    def inaccessible_callback(self, name, **kwargs):
        if self.pass_enabled:
            flash("Admin page is restricted", 'error')
            return redirect(url_for('/.home_page'))

        flash('Please enter your login and password', 'info')
        return redirect(url_for('user.login', next='/admin'))






