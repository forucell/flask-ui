from .base import BaseView

class RoleView(BaseView):
    page_size = 10
    create_modal = True
    edit_modal = True
    details_modal = True

    can_view_details = True
    can_set_page_size = True



