from flask import Blueprint
from vendor.models import User


vendor_views = Blueprint('vendor', __name__, url_prefix='/')


@vendor_views.route('/')
def index():
    context = User.query().count()
    return context
