# Test 3 - POST /register captures the submitted values

import unittest

from app import app


class TestPostCapture(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_post_shows_full_name_and_username(self):
        response = self.client.post(
            "/register",
            data={
                "full_name": "Jane Doe",
                "username": "test_user_CSE",
                "password": "TestPassword123",
                "confirm_password": "TestPassword123",
            },
        )
        html = response.get_data(as_text=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn("Jane Doe", html)
        self.assertIn("test_user_CSE", html)

    def test_plain_text_password_is_never_displayed(self):
        response = self.client.post(
            "/register",
            data={
                "full_name": "Jane Doe",
                "username": "test_user_CSE",
                "password": "TestPassword123",
                "confirm_password": "TestPassword123",
            },
        )
        self.assertNotIn("TestPassword123", response.get_data(as_text=True))


if __name__ == "__main__":
    unittest.main()
