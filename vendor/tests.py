from flask.ext.testing import TestCase
import unittest
from vendor import create_app
from vendor.models import db, User

if __name__ == '__main__':
    unittest.main()


class BaseTestCase(TestCase):
    """A base test case."""

    def create_app(self):
        # app = create_app('vendor.config.TestConfig')
        return create_app('vendor.config.TestConfig')

    def setUp(self):
        db.create_all()
        db.session.add(User("admin", "ad@min.com"))
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class FlaskTestCase(BaseTestCase):
    def test_index(self):
        response = self.client.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)


