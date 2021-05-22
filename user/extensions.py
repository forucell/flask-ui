from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from passlib.context import CryptContext

from flask_uploads import UploadSet, IMAGES

from flask_login import LoginManager
from flask_admin import Admin

db = SQLAlchemy()
migrate = Migrate()
pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")
login_manager = LoginManager()

upload_set = UploadSet('images', IMAGES)

from user.views.my_admin import MyAdminView
admin = Admin(index_view=MyAdminView(), template_mode='bootstrap3', name='Paycheck')