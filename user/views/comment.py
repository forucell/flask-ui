from flask_admin.contrib.sqla import ModelView


class CommentView(ModelView):
    create_modal = True
    edit_modal = True
