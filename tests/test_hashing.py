# Test 5 - bcrypt hashing and the confirmation message

import re
import unittest

import bcrypt

from app import app


class TestHashing(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.password = "TestPassword123"
        self.html = self.client.post(
            "/register",
            data={
                "full_name": "Jane Doe",
                "username": "test_user_CSE",
                "password": self.password,
                "confirm_password": self.password,
            },
        ).get_data(as_text=True)

    def extract_hash(self):
        match = re.search(r"\$2[aby]\$\d{2}\$[./A-Za-z0-9]{53}", self.html)
        self.assertIsNotNone(match, "No bcrypt hash found on the page")
        return match.group(0)

    def test_confirmation_shows_name_username_and_hash(self):
        self.assertIn("Registration Successful", self.html)
        self.assertIn("Jane Doe", self.html)
        self.assertIn("test_user_CSE", self.html)
        self.extract_hash()

    def test_hash_verifies_against_original_password(self):
        hashed = self.extract_hash()
        self.assertTrue(bcrypt.checkpw(self.password.encode("utf-8"), hashed.encode("utf-8")))

    def test_hash_does_not_verify_against_wrong_password(self):
        hashed = self.extract_hash()
        self.assertFalse(bcrypt.checkpw(b"WrongPassword123", hashed.encode("utf-8")))

    def test_plain_text_password_is_not_displayed(self):
        self.assertNotIn(self.password, self.html)

    def test_same_password_produces_different_hashes_each_time(self):
        first = self.extract_hash()
        second_html = self.client.post(
            "/register",
            data={
                "full_name": "Jane Doe",
                "username": "test_user_CSE",
                "password": self.password,
                "confirm_password": self.password,
            },
        ).get_data(as_text=True)
        second = re.search(r"\$2[aby]\$\d{2}\$[./A-Za-z0-9]{53}", second_html).group(0)
        self.assertNotEqual(first, second)


if __name__ == "__main__":
    unittest.main()
