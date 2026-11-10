# Test 4 - input validation

import unittest

from app import app

USERNAME_ERROR = "Username must contain only letters, numbers, and underscores."
PASSWORD_ERROR = "Password must be at least 8 characters long and include both letters and numbers."
MISMATCH_ERROR = "Password and confirm password must match."


class TestValidation(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def post(self, full_name="Jane Doe", username="test_user_CSE",
             password="TestPassword123", confirm_password=None):
        if confirm_password is None:
            confirm_password = password
        response = self.client.post(
            "/register",
            data={
                "full_name": full_name,
                "username": username,
                "password": password,
                "confirm_password": confirm_password,
            },
        )
        return response.get_data(as_text=True)

    def test_valid_input_has_no_errors(self):
        html = self.post()
        self.assertNotIn('class="error"', html)
        self.assertIn("Registration Successful", html)

    def test_username_with_space_is_rejected(self):
        self.assertIn(USERNAME_ERROR, self.post(username="bad name"))

    def test_username_with_special_character_is_rejected(self):
        self.assertIn(USERNAME_ERROR, self.post(username="bad!name"))

    def test_empty_username_is_rejected(self):
        self.assertIn(USERNAME_ERROR, self.post(username=""))

    def test_username_with_underscores_and_numbers_is_accepted(self):
        self.assertNotIn(USERNAME_ERROR, self.post(username="user_123_ABC"))

    def test_password_too_short_is_rejected(self):
        self.assertIn(PASSWORD_ERROR, self.post(password="Abc123"))

    def test_password_without_numbers_is_rejected(self):
        self.assertIn(PASSWORD_ERROR, self.post(password="OnlyLetters"))

    def test_password_without_letters_is_rejected(self):
        self.assertIn(PASSWORD_ERROR, self.post(password="12345678"))

    def test_password_mismatch_is_rejected(self):
        self.assertIn(MISMATCH_ERROR, self.post(confirm_password="TestPassword124"))

    def test_multiple_errors_are_all_shown(self):
        html = self.post(username="bad name", password="abc", confirm_password="xyz")
        self.assertIn(USERNAME_ERROR, html)
        self.assertIn(PASSWORD_ERROR, html)
        self.assertIn(MISMATCH_ERROR, html)

    def test_failed_validation_does_not_show_success(self):
        self.assertNotIn("Registration Successful", self.post(username="bad name"))

    def test_form_keeps_name_and_username_after_error(self):
        html = self.post(full_name="Jane Doe", username="bad name")
        self.assertIn('value="Jane Doe"', html)
        self.assertIn('value="bad name"', html)


if __name__ == "__main__":
    unittest.main()
