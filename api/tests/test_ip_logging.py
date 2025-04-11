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
        "api.middleware.IPLoggingMiddleware",
    ]
)
class IPLoggingMiddlewareTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.log_file = "logs/ip_log.log"

        # Clean up old log file before testing
        if os.path.exists(self.log_file):
            os.remove(self.log_file)

    def test_ip_logging(self):
        # Trigger the login view (no credentials = 400 expected)
        response = self.client.post("/api/users/login/", {}, content_type="application/json")
        self.assertEqual(response.status_code, 400)

        # Assert log file was created
        self.assertTrue(os.path.exists(self.log_file))

        # Check content of the log file
        with open(self.log_file, "r") as f:
            logs = f.read()

        self.assertIn("127.0.0.1", logs)
