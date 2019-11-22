from django.test import TestCase

from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """pass"""

    def test_create_user_with_email_successful(self):
        """test creating a new user with a email"""
        email = 'test@app.com'
        password = 'test@123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email(self):
        """Test the email for new user normalized"""

        email = 'test@ALIKHORSAND.IR'
        user = get_user_model().objects.create_user(email, 'test@123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_super_user(self):
        """test creating a new super user"""

        user = get_user_model().objects.create_superuser(
            'test@alikhorsand.ir',
            'test@123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
