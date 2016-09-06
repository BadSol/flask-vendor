from flask import Blueprint, render_template
from flask_login import login_required


vendor_views = Blueprint('vendor', __name__, url_prefix='/')


@vendor_views.route('/')
@login_required
def index():
    """
    Basic index view
    Uses @login_required decorator to restrict view access for anonymous users
    """

    return render_template('index.html')
