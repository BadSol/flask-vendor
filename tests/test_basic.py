import unittest

from base import BaseTestCase
from vendor.models import User, bcrypt


class FlaskTestCase(BaseTestCase):
    def test_index(self):
        response = self.client.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_setUp(self):
        user = User.query.first()
        self.assertEqual(user.name, 'admin')

    def test_bcrypt_password_hash(self):
        password = "@WD3ef6%%%%$GASDA"
        pw_hash = bcrypt.generate_password_hash(password)

        self.assertTrue(bcrypt.check_password_hash(pw_hash, password))


if __name__ == '__main__':
    unittest.main()
