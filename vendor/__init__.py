from flask import Flask
# from config import Config


def create_app(config='vendor.config.DevelopmentConfig'):
    app = Flask(__name__)
    app.config.from_object(config)

    from vendor.models import db, bcrypt
    db.init_app(app)
    bcrypt.init_app(app)

    from vendor.views import vendor_views

    app.register_blueprint(vendor_views)

    return app

