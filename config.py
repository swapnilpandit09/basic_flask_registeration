import os

class ConfigClass(object):
    # Flask settings
    # import ipdb; ipdb.set_trace()
    SECRET_KEY =              os.getenv('SECRET_KEY',       'THIS IS AN INSECURE SECRET')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL',     'sqlite:///basic_app.sqlite')
    CSRF_ENABLED = True

    # Flask-Mail settings
    MAIL_USERNAME = 'noreply@vertisinfotech.com'
    MAIL_PASSWORD = ''
    MAIL_DEFAULT_SENDER = 'noreply@vertisinfotech.com'
    MAIL_SERVER = 'smtp.vertis'
    MAIL_PORT = ''
    MAIL_USE_SSL = False

    # Flask-User settings
    USER_APP_NAME = "AppName"
    # USER_LOGIN_TEMPLATE  = 'flask_user/login_or_register.html'             # Used by email templates
    # USER_REGISTER_URL    = '/user/register'
