
from flask import Blueprint, render_template_string, redirect, url_for, render_template

from flask_user import login_required, roles_required

blueprint = Blueprint("/", __name__, url_prefix="")


# The Home page is accessible to anyone
@blueprint.route('/')
@login_required    # Use of @login_required decorator
def home_page():
    name = 'Home Page'
    return render_template('new/member.html', var1=name)
    # return redirect(url_for('/.admin_page'))
    # return redirect('admin')


# The Members page is only accessible to authenticated users
@blueprint.route('/users')
@roles_required('user')  # Use of @roles_required decorator
def user_page():
    name = 'User Page'
    return render_template('new/member.html', var1=name)

# The Members page is only accessible to authenticated users
@blueprint.route('/agents')
@roles_required('agent')  # Use of @roles_required decorator
def agent_page():
    name = 'Agent Page'
    return render_template('new/member.html', var1=name)

# The Admin page requires an 'Admin' role.
@blueprint.route('/admin')
@roles_required('admin')  # Use of @roles_required decorator
def admin_page():
    pass
#
# # The Admin page requires an 'Admin' role.
# @blueprint.route('/admin/user')
# @roles_required('admin')  # Use of @roles_required decorator
# def user_page():
#     pass

