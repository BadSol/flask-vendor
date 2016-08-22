from flask import Blueprint
from vendor.models import User, db


vendor_views = Blueprint('vendor', __name__, url_prefix='/')


@vendor_views.route('/')
def index():
    # context = db.session.query(User).all()  # both doesn't work TypeError: 'User' object is not callable
    context = User.query().all()  # TypeError: 'BaseQuery' object is not callable
    return context
