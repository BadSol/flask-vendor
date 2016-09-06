from flask import Flask
from config import BaseConfig


def create_app(cfg='vendor.config.DevelopmentConfig'):
    """
    Creates app instance which allows benefits of using app factories.

    :param cfg: Location of config file
    :return: app object
    """
    app = Flask(__name__)
    app.config.from_object(cfg)

    from vendor.models import db, bcrypt
    db.init_app(app)
    bcrypt.init_app(app)

    from vendor.views import vendor_views
    from vendor.user.views import user_views, login_manager

    login_manager.login_view = "user.login"
    login_manager.init_app(app)

    app.register_blueprint(vendor_views)
    app.register_blueprint(user_views)

    from vendor.models import User

    return app
