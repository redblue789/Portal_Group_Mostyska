from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Profile


class AuthFlowTests(TestCase):
    def test_home_page_is_accessible(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_register_page_is_accessible(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)

    def test_dashboard_requires_login(self):
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 302)
        self.assertIn('/login/', response.url)

    def test_roles_are_defined_for_users_moderators_and_admins(self):
        user = User.objects.create_user(username='student', password='testpass123')
        moderator = User.objects.create_user(username='moderator', password='testpass123')
        admin = User.objects.create_user(username='admin', password='testpass123')

        user.profile.role = 'user'
        moderator.profile.role = 'moderator'
        admin.profile.role = 'admin'

        user.profile.save()
        moderator.profile.save()
        admin.profile.save()

        self.assertEqual(user.profile.role, 'user')
        self.assertEqual(moderator.profile.role, 'moderator')
        self.assertEqual(admin.profile.role, 'admin')

    def test_superuser_gets_admin_role_automatically(self):
        admin = User.objects.create_superuser(
            username='teacher',
            email='teacher@example.com',
            password='testpass123',
        )

        self.assertEqual(admin.profile.role, 'admin')
