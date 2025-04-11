from django.test import TestCase, Client


class RateLimitingTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = "/api/users/login/"
        self.payload = {
            "email": "nonexistent@example.com",
            "password": "wrongpassword"
        }

    def test_unauthenticated_rate_limit(self):
        # First request (should return 400 due to bad credentials)
        response1 = self.client.post(self.login_url, self.payload, content_type="application/json")
        self.assertEqual(response1.status_code, 400)

        # Second request (should be rate limited)
        response2 = self.client.post(self.login_url, self.payload, content_type="application/json")
        self.assertEqual(response2.status_code, 429)
        
