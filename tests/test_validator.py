import unittest

from validator import validate_email, validate_phone


class TestValidator(unittest.TestCase):
    def test_validate_email(self):
        self.assertTrue(validate_email("test@example.com"))
        self.assertFalse(validate_email("invalid"))

    def test_validate_phone(self):
        self.assertTrue(validate_phone("+79991234567"))
        self.assertFalse(validate_phone("89991234567"))
        self.assertFalse(validate_phone("+7999123"))

    def test_validate_phone_formatting(self):
        self.assertTrue(validate_phone("79991234567"))
        self.assertTrue(validate_phone("+7 999-123-45-67"))
        self.assertFalse(validate_phone(""))
        self.assertFalse(validate_phone("+7999123456a"))


if __name__ == "__main__":
    unittest.main()
