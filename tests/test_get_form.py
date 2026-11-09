# Test 2 - GET /register shows the empty registration form

import unittest

from app import app


class TestGetForm(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.html = self.client.get("/register").get_data(as_text=True)

    def test_has_all_form_fields(self):
        for field_name in ("full_name", "username", "password", "confirm_password"):
            self.assertIn(f'name="{field_name}"', self.html)

    def test_password_fields_are_masked(self):
        self.assertIn('type="password" id="password"', self.html)
        self.assertIn('type="password" id="confirm_password"', self.html)

    def test_has_register_button(self):
        self.assertIn("Register</button>", self.html)

    def test_form_posts_to_register(self):
        self.assertIn('method="POST"', self.html)
        self.assertIn('action="/register"', self.html)

    def test_form_starts_empty_with_no_messages(self):
        self.assertNotIn("Registration Successful", self.html)
        self.assertNotIn('class="error"', self.html)


if __name__ == "__main__":
    unittest.main()
