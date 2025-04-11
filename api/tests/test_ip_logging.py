from django.test import TestCase, Client, override_settings
import os


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
class IPLoggingMiddlewareTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.log_file = "logs/ip_log.log"

    def test_ip_logging(self):
        response = self.client.post("/api/login/", {}, content_type="application/json")
        self.assertEqual(response.status_code, 400)  # because no credentials

        self.assertTrue(os.path.exists(self.log_file))

        with open(self.log_file, "r") as f:
            logs = f.read()
        self.assertIn("127.0.0.1", logs)
        
