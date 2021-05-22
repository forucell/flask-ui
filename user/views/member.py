from flask_admin.contrib.sqla import ModelView


class MemberView(ModelView):
    create_modal = True
    edit_modal = True

    column_display_all_relations = True

    # def validate_form(self, form):
    #     pass
