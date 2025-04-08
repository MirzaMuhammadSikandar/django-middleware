from django.test import TestCase, Client


class RateLimitingTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_unauthenticated_rate_limit(self):
        for i in range(2):  # limit is 1 per minute
            response = self.client.get("/api/login/")
        self.assertEqual(response.status_code, 429)
