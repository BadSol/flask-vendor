from flask import Blueprint, render_template
from vendor.models import User, db
from flask_login import LoginManager

login_manager = LoginManager()

vendor_views = Blueprint('vendor', __name__, url_prefix='/')


@vendor_views.route('/')
def index():
    # context = db.session.query(User).all()  # both doesn't work TypeError: 'User' object is not callable
    # user = User.query.all()  # TypeError: 'BaseQuery' object is not callable
    user = db.session.query(User).first()

    return render_template('index.html', user=user)
