from flask import Blueprint, render_template, request, redirect, url_for
from vendor.models import User, bcrypt, db
from flask_login import LoginManager, login_user, login_required, current_user, logout_user

login_manager = LoginManager()

user_views = Blueprint('user', __name__, url_prefix='/')


@user_views.route('login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        user_obj = User.query.filter(User.email == request.form['email'].lower()).one_or_none()
        user = load_user(user_obj.get_id())  # todo: refactor this, load_user needs unicode id of object as argument

        if user is not None and validate_login(user, request.form['password']):  # Validate user:
            login_user(user)
            return redirect(request.args.get('next') or url_for('vendor.index'))  # todo: check if next page works
        # Warning: You MUST validate the value of the next parameter.
        # If you do not, your application will be vulnerable to open redirects.

        else:
            return render_template('login.html', error='User doesn\'t exist, or wrong password')

    return render_template('login.html')


@user_views.route('logout')
def logout():
    logout_user()
    return redirect(url_for('vendor.index'))


@user_views.route('register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user_email = request.form['email'].lower()

        if check_if_user_exist(user_email):

            error = 'Email already exists'
            return render_template('register.html', error=error)

        user_name = request.form['name'].title()
        user_password = request.form['password']

        new_user = User(name=user_name, email=user_email, password=user_password)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('user.login'))

    return render_template('register.html')



@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == user_id).one_or_none()


def validate_login(user, password):
    return bcrypt.check_password_hash(user.password, password)


def check_if_user_exist(user_email):
    if User.query.filter(User.email == user_email).one_or_none():
        return True
    return False
