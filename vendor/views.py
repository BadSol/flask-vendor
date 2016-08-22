from flask import Blueprint
from vendor.models import User


vendor_views = Blueprint('vendor', __name__, url_prefix='/')


@vendor_views.route('/')
def index():
    return "Aww Yiss"


@vendor_views.route('main')
def main():
    context = User.query.all()
    return 'main: ' + '\n'.join(context)
