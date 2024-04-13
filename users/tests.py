from django.contrib.auth import get_user_model
from django.test import TestCase


class UserManagerTests(TestCase):
    
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(email='test@mail.com', password='test')
        self.assertEqual(user.email, 'test@mail.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        try:
            self.assertIsNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email='')
        with self.assertRaises(ValueError):
            User.objects.create_user(email='', password='test')
    
    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(email='superuser@mail.com', password='test')
        self.assertEqual(admin_user.email, 'superuser@mail.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        try:
            self.assertIsNone(admin_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email='superuser@mail.com', password='test', is_superuser=False)
