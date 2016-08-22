from flask import Flask
from config import Config


def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = Config.DATABASE_URI

    from vendor.models import db
    db.init_app(app)

    from vendor.views import vendor_views

    app.register_blueprint(vendor_views)

    return app

