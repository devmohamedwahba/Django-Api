from django.test import TestCase
from django.contrib.auth import get_user_model
from .. import models


def sample_user(email="Test@gmail.com", password="P@ssw0rd"):
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """ test creating new user with email """
        email = "test@gmail.com"
        password = "P@ssw0rd1"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalize(self):
        email = "test@Gmail.com"
        user = get_user_model().objects.create_user(
            email=email,
            password="test123"
        )
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "P@ssw0rd")

    def test_create_super_user(self):
        email = "test@gmail.com"
        password = "P@ssw0rd"
        user = get_user_model().objects.create_superuser(
            email=email,
            password=password
        )
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

    def test_tag_str(self):
        tag = models.Tag.objects.create(
            user=sample_user(),
            name="Vegan"

        )
        self.assertEqual(str(tag), tag.name)
