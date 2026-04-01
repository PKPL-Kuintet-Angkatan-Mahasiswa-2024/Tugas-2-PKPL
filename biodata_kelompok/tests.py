from allauth.socialaccount.models import SocialAccount
from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import Client, TestCase

from biodata_kelompok.models import Biodata
from biodata_kelompok.views import is_authorized

User = get_user_model()


class AuthorizationTest(TestCase):
    def setUp(self):
        self.client = Client()

        self.allowed_email = settings.GROUP_MEMBER_EMAILS[0]

        self.authorized_user = User.objects.create_user(
            username="authorized", email=self.allowed_email, password="testpass123"
        )

        self.unauthorized_user = User.objects.create_user(
            username="unauthorized",
            email="notingroup@example.com",
            password="testpass123",
        )

        SocialAccount.objects.create(
            user=self.authorized_user, provider="google", uid="123"
        )

        SocialAccount.objects.create(
            user=self.unauthorized_user, provider="google", uid="456"
        )

        Biodata.objects.create(user=self.authorized_user, bio="Authorized bio")
        Biodata.objects.create(user=self.unauthorized_user, bio="Unauthorized bio")

    def test_is_authorized_true(self):
        self.assertTrue(is_authorized(self.authorized_user))

    def test_is_authorized_false_not_in_group(self):
        self.assertFalse(is_authorized(self.unauthorized_user))

    def test_edit_denied_for_unauthorized_user(self):
        self.client.login(username="unauthorized", password="testpass123")
        response = self.client.get("/edit-tampilan/")
        self.assertEqual(response.status_code, 302)

    def test_edit_allowed_for_authorized_user(self):
        self.client.login(username="authorized", password="testpass123")
        response = self.client.get("/edit-tampilan/")
        self.assertEqual(response.status_code, 200)

