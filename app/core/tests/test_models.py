from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'test@londonappdev.com'
        password = 'Password123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """test user email normalization"""
        email = 'test@lonDonappdev.com'
        user = get_user_model().objects.create_user(
            email=email,
            password='wqefasdfoasdf'
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_validate_email(self):
        """test creating user without email"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_superuser(self):
        """Test new superuser creation"""
        user = get_user_model().objects.create_superuser(
            email='test@lonDonappdev.com',
            password='1234'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
