from flask import Blueprint, render_template, request, redirect, url_for, flash
from vendor.models import User, db, bcrypt
from flask_login import LoginManager, login_user, login_required, current_user, logout_user

login_manager = LoginManager()

vendor_views = Blueprint('vendor', __name__, url_prefix='/')


@vendor_views.route('/')
@login_required
def index():
    # context = db.session.query(User).all()  # both doesn't work TypeError: 'User' object is not callable
    # user = User.query.all()  # TypeError: 'BaseQuery' object is not callable
    user = db.session.query(User).first()

    return render_template('index.html', user=user.email)


@vendor_views.route('login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        user_obj = User.query.filter(User.email == request.form['email'].lower()).one_or_none()
        user = load_user(user_obj.get_id())  # todo: refactor this, load_user needs unicode id of object as argument

        if user is not None and validate_login(user, request.form['password']):  # Validate user:
            login_user(user)
            # flash('Logged in successfully')  # todo: learn how flash works
            return redirect(request.args.get('next') or url_for('vendor.index'))  # todo: check if next page works
        # Warning: You MUST validate the value of the next parameter.
        # If you do not, your application will be vulnerable to open redirects.

        else:
            return render_template('login.html', error='User doesn\'t exist, or wrong password')

    return render_template('login.html')


@vendor_views.route('logout')
def logout():
    logout_user()
    return redirect(url_for('vendor.index'))



@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == user_id).one_or_none()


def validate_login(user, password):
    return bcrypt.check_password_hash(user.password, password)
