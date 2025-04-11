from django.test import TestCase, Client, override_settings
from api.models import User


@override_settings(
    MIDDLEWARE=[
        "django.middleware.security.SecurityMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
    ]
)
class AuthViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user_data = {
            "email": "test2@example.com",
            "password": "test12345",
            "role": "gold",
        }

    def test_register(self):
        response = self.client.post(
            "/api/register/", self.user_data, content_type="application/json"
        )
        self.assertEqual(response.status_code, 201)

    def test_login_logout(self):
        self.client.post(
            "/api/register/", self.user_data, content_type="application/json"
        )
        login_response = self.client.post(
            "/api/login/", self.user_data, content_type="application/json"
        )
        self.assertEqual(login_response.status_code, 200)

        logout_response = self.client.post("/api/logout/")
        self.assertEqual(logout_response.status_code, 200)
        
