import os
import uuid

from flask import Markup
from flask_admin import form
from werkzeug.utils import secure_filename
from wtforms import validators

from flask_admin.contrib.sqla import ModelView

# return <img ...> tag with image url
def _list_thumbnail(view, context, model, name):
    if not model.filename:
        return ''
    return Markup(
        '<img src="{model.url}" style="width: 150px;">'.format(model=model)
    )


# Generate random unique filename
def _imagename_uuid1_gen(obj, file_data):
    _, ext = os.path.splitext(file_data.filename)
    uid = uuid.uuid1()
    return secure_filename('{}{}'.format(uid, ext))

class ImageView(ModelView):
    create_modal = True
    edit_modal = True

    can_edit = True
    can_view_details = True
    column_list = ['image', 'name']

    # column_editable_list = ['name', 'users']

    # column_list['image'] == column_formatters['image']

    # display returned markup .e.g. image
    column_formatters = {
        'image': _list_thumbnail
    }

    # add extra field
    form_extra_fields = {
        'filename': form.ImageUploadField(
            label='Image',  # name of the extra field .e.g. in the create tab
            base_path='user/static/images',  # set path to store an image
            url_relative_path='images/',  # set path to display image on edit tab
            namegen=_imagename_uuid1_gen,
            validators=[validators.DataRequired()],
        )
    }

    column_display_all_relations = True



    def get_column_list(self):
        return self.column_list