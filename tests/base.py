from flask_testing import TestCase

from vendor import create_app
from vendor.models import db, User


class BaseTestCase(TestCase):
    """A base test case."""

    def create_app(self):
        app = create_app('vendor.config.TestConfig')
        return app

    def setUp(self):
        db.create_all()
        db.session.add(User("admin", "ad@min.com", "password"))
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
