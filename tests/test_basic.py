import unittest

from base import BaseTestCase
from flask import url_for
from vendor.models import User, bcrypt
from vendor.user.views import check_if_user_exist
from flask_login import current_user


class FlaskTestCase(BaseTestCase):
    def test_set_up(self):
        user = User.query.first()
        self.assertEqual(user.name, 'admin')

    def test_bcrypt_password_hash(self):
        password = "@WD3ef6%%%%$GASDA"
        pw_hash = bcrypt.generate_password_hash(password)

        self.assertTrue(bcrypt.check_password_hash(pw_hash, password))


class ViewTestCase(BaseTestCase):
    # test index view
    def test_index(self):
        response = self.client.get(url_for('vendor.index'), content_type='html/text', follow_redirects=True)
        self.assertIn(' Please login', response.data)

    # test login view
    def test_login_view(self):
        response = self.client.get(url_for('user.login'), content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertIn(' Please login', response.data)

    # test register view
    def test_register_view(self):
        response = self.client.get(url_for('user.register'), content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Register form:', response.data)

    # test index view as logged user
    def test_index_authorized(self):
        with self.client:
            response = self.client.post(url_for('user.login'),
                                        data=dict(email=self.basic_user_email,
                                                  password=self.basic_user_password),
                                        follow_redirects=True
                                        )
            self.assertEqual(current_user.name, self.basic_user_name)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Hello, World!' and 'Log out' and 'Hi {}!'.format(self.basic_user_name), response.data)

    # Ensure that logout view works
    def test_logout(self):
        with self.client:
            self.client.post(url_for('user.login'),
                             data=dict(email=self.basic_user_email,
                                       password=self.basic_user_password),
                             follow_redirects=True
                             )

            self.assertEqual(current_user.name, self.basic_user_name)
            self.client.get(url_for('user.logout'))
            self.assertFalse(current_user.is_authenticated)

    # Ensure that user registration works
    def test_register_new_user(self):
        self.client.post(url_for('user.register'),
                         data=dict(name='test_name',
                                   email='test_email@test.com',
                                   password='test_password'),
                         follow_redirects=True
                         )
        user = User.query.filter(User.email == 'test_email@test.com').one_or_none()

        self.assertEqual(user.name, 'test_name'.title())

    # Ensure registering with already existing email fails
    def test_register_already_existing_user(self):
        response = self.client.post(url_for('user.register'),
                                    data=dict(name='test_name',
                                              email='test_email@test.com',
                                              password='test_password'),
                                    follow_redirects=True
                                    )
        self.assertEqual(response.data, 'Email already exists')

if __name__ == '__main__':
    unittest.main()
