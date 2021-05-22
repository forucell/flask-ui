# Class-based application configuration
class ConfigClass(object):
    """ Flask application config """

    # Flask settings
    SECRET_KEY = '809HHKDOUHF53D5KFJHBNS99886HH6G68HMMMSDS'

    # Flask-SQLAlchemy settings
    SQLALCHEMY_DATABASE_URI = 'sqlite:////Users/sam/PycharmProjects/flask-ui/test.db'    # File-based SQL database
    SQLALCHEMY_TRACK_MODIFICATIONS = False    # Avoids SQLAlchemy warning
    CSRF_ENABLED = True

    # Flask-Mail SMTP server settings
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USE_TLS = False
    MAIL_USERNAME = ''
    MAIL_PASSWORD = ''
    MAIL_DEFAULT_SENDER = '"MyApp" <noreply@example.com>'

    # Flask-User settings
    USER_APP_NAME = "Flask-User Basic App"      # Shown in and email templates and page footers
    USER_ENABLE_EMAIL = True        # Enable email authentication
    USER_ENABLE_USERNAME = True    # Enable username authentication
    USER_EMAIL_SENDER_NAME = USER_APP_NAME
    USER_EMAIL_SENDER_EMAIL = "noreply@example.com"

    USER_AFTER_REGISTER_ENDPOINT = 'user.login'
    USER_AFTER_LOGOUT_ENDPOINT = 'user.login'

    USER_ENABLE_CHANGE_PASSWORD = True
    USER_SEND_PASSWORD_CHANGED_EMAIL = True

    USER_ENABLE_CHANGE_USERNAME = True
    USER_SEND_USERNAME_CHANGED_EMAIL = True

    USER_REQUIRE_RETYPE_PASSWORD = True

    USER_PASSLIB_CRYPTCONTEXT_SCHEMES = ['pbkdf2_sha256']

    # CACHE_TYPE = 'null'

    MAX_CONTENT_LENGTH = 16777216

    UPLOADED_IMAGES_DEST = 'user/static/images'

    UPLOADED_IMAGES_URL = '/static/images/'

    UPLOADS_DEFAULT_DEST = 'static/images'