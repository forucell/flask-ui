from .base import BaseView
from user.extensions import pwd_context

class UserView(BaseView):
    page_size = 10
    create_modal = True
    edit_modal = True
    details_modal = True

    can_view_details = True
    can_set_page_size = True

    column_details_exclude_list = ['password']

    def on_model_change(self, form, model, is_created):
        # model.password = generate_password_hash(model.password, method='sha256')
        model.password = pwd_context.hash(model.password)

    def on_form_prefill(self, form, id):
        form.password.data = '******'

    column_editable_list = ['email', 'active', 'images']

    column_exclude_list = ['password', 'roles', 'first_name', 'last_name', 'email_confirmed_at']

    column_display_all_relations = True

