from .base import BaseView

class UserRoleView(BaseView):
    page_size = 10
    create_modal = True
    edit_modal = True
    details_modal = True

    can_view_details = True
    can_set_page_size = True

    column_list = ['user_id', 'role_id']



