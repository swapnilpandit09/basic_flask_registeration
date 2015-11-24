from flask import Flask, render_template
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_user import login_required, UserManager, UserMixin, SQLAlchemyAdapter
from flask.ext.user.forms import RegisterForm

from wtforms.fields.core import StringField
from wtforms.validators import Required

from config import ConfigClass


def create_app():
    """ Flask application factory """

    # Setup Flask app and app.config
    app = Flask(__name__)
    app.config.from_object(__name__ + '.ConfigClass')

    # Initialize Flask extensions
    db = SQLAlchemy(app)  # Initialize Flask-SQLAlchemy
    mail = Mail(app)  # Initialize Flask-Mail


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

    class MyRegisterForm(RegisterForm):
        first_name = StringField('First name', validators=[Required('First name is required')])
        last_name = StringField('Last name', validators=[Required('Last name is required')])

    db.create_all()

    db_adapter = SQLAlchemyAdapter(db, User)
    user_manager = UserManager(db_adapter, app, register_form=MyRegisterForm)

    @app.route('/')
    def home_page():
        return render_template('base.html')


    @app.route('/members')
    @login_required
    def members_page():
        return render_template('member.html')

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)
