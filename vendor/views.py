from flask import Blueprint, render_template, request, redirect, url_for
from vendor.models import User, db, bcrypt
from flask_login import LoginManager

login_manager = LoginManager()

vendor_views = Blueprint('vendor', __name__, url_prefix='/')


@vendor_views.route('/')
def index():
    # context = db.session.query(User).all()  # both doesn't work TypeError: 'User' object is not callable
    # user = User.query.all()  # TypeError: 'BaseQuery' object is not callable
    user = db.session.query(User).first()

    return render_template('index.html', user=user.email)


@vendor_views.route('login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        user = load_user(request.form['email'])
        if validate_login(user, request.form['password']):
            print 'User {} logged in!'.format(user.name)
        else:
            redirect(url_for('vendor.login'))

    else:
        return render_template('login.html')


@login_manager.user_loader
def load_user(user_email):
    return User.query.filter(User.email == user_email).one_or_none()


def validate_login(user, password):
    return bcrypt.check_password_hash(user.password, password)
