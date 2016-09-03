from flask_testing import TestCase

from vendor import create_app
from vendor.models import db, User


class BaseTestCase(TestCase):
    """A base test case."""
    basic_user_name = 'admin'
    basic_user_email = 'ad@min.com'
    basic_user_password = 'password'

    def create_app(self):
        app = create_app('vendor.config.TestConfig')
        return app

    def setUp(self):
        db.create_all()
        db.session.add(User(self.basic_user_name, self.basic_user_email, self.basic_user_password))
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
