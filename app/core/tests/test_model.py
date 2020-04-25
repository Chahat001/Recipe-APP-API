from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_email_successful(self):
        """ Test Creating a new user with email is successful """
        email = 'chahat001"gmail.com'
        password = '12345'

        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """ Test the email for new user is normalized"""
        email = 'test@GMAIL.com'
        password = '9815736711'
        user = get_user_model().objects.create_user(
            email = email,
            password = password
         )

        self.assertEqual(user.email,email.lower())

    def test_new_user_inavlid_email(self):
        """ Test that new user cannot be created without a email"""
        with self.assertRaises(ValueError):
            user = get_user_model().objects.create_user(None, '12345')

    def test_create_new_superuser(self):
        """ Test creating a new Super User """
        user = get_user_model().objects.create_superuser(
        email = 'grewal001"gmail.com', password = '12345'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
