# from flask import Flask, render_template
# from flask.ext.sqlalchemy import SQLAlchemy

import os
from flask import Flask, render_template_string, render_template
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_user import login_required, UserManager, UserMixin, SQLAlchemyAdapter

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/myflask.db'
# db = SQLAlchemy(app)


class ConfigClass(object):
    # Flask settings
    # import ipdb; ipdb.set_trace()
    SECRET_KEY =              os.getenv('SECRET_KEY',       'THIS IS AN INSECURE SECRET')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL',     'sqlite:///basic_app.sqlite')
    CSRF_ENABLED = True

    # Flask-Mail settings
    MAIL_USERNAME =           os.getenv('MAIL_USERNAME',        'email@example.com')
    MAIL_PASSWORD =           os.getenv('MAIL_PASSWORD',        'password')
    MAIL_DEFAULT_SENDER =     os.getenv('MAIL_DEFAULT_SENDER',  '"MyApp" <noreply@example.com>')
    MAIL_SERVER =             os.getenv('MAIL_SERVER',          'smtp.gmail.com')
    MAIL_PORT =           int(os.getenv('MAIL_PORT',            '465'))
    MAIL_USE_SSL =        int(os.getenv('MAIL_USE_SSL',         True))

    # Flask-User settings
    USER_APP_NAME        = "AppName"                # Used by email templates


def create_app():
    """ Flask application factory """
    
    # Setup Flask app and app.config
    app = Flask(__name__)
    app.config.from_object(__name__+'.ConfigClass')

    # Initialize Flask extensions
    db = SQLAlchemy(app)                            # Initialize Flask-SQLAlchemy
    mail = Mail(app)                                # Initialize Flask-Mail



    class User(db.Model, UserMixin):
        id = db.Column(db.Integer, primary_key=True)

        # User authentication information
        username = db.Column(db.String(50), nullable=False, unique=True)
        password = db.Column(db.String(255), nullable=False, server_default='')
        reset_password_token = db.Column(db.String(100), nullable=False, server_default='')

        # User email information
        email = db.Column(db.String(255), nullable=False, unique=True)
        confirmed_at = db.Column(db.DateTime())

        # User information
        active = db.Column('is_active', db.Boolean(), nullable=False, server_default='0')
        first_name = db.Column(db.String(100), nullable=False, server_default='')
        last_name = db.Column(db.String(100), nullable=False, server_default='')


    db.create_all()

    db_adapter = SQLAlchemyAdapter(db, User)        # Register the User model
# import ipdb; ipdb.set_trace()
# user_manager = UserManager(db_adapter, app)   



    @app.route('/')
    def home_page():
        return render_template('login.html')


    @app.route('/members')
    @login_required                                 # Use of @login_required decorator
    def members_page():
        return render_template('member.html')

    return app

if __name__=='__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)



# @app.route('/')
# def hello_world():
#     return 'Hello World!'

# @app.route('/signup')
# def signup():
#     return 'signup form'

# @app.route('/login')
# def show_the_login_form():
# 	return render_template('login.html')

# def login():
#     if request.method == 'POST':
#         do_the_login()
#     else:
#         show_the_login_form()


# def do_the_login(**kwargs):
# 	pass



# class User(db.Model, UserMixin):
#     id = db.Column(db.Integer, primary_key=True)

#     # User Authentication information
#     username = db.Column(db.String(50), nullable=False, unique=True)
#     password = db.Column(db.String(255), nullable=False, default='')

#     # User Email information
#     email = db.Column(db.String(255), nullable=False, unique=True)
#     confirmed_at = db.Column(db.DateTime())

#     # User information
#     first_name = db.Column(db.String(50), nullable=False, default='')
#     last_name = db.Column(db.String(50), nullable=False, default='')


# db_adapter = SQLAlchemyAdapter(db, User)
# user_manager = UserManager(db_adapter, app)


# if __name__ == '__main__':
#     app.debug = True
#     app.run()
