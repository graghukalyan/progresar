import unittest
from app.utils.helpers import format_email

class TestHelpers(unittest.TestCase):
    def test_format_email(self):
        self.assertEqual(format_email(" Test@Example.com "), "test@example.com")
        self.assertEqual(format_email("user@domain.com"), "user@domain.com")
        self.assertEqual(format_email(" USER@DOMAIN.COM "), "user@domain.com")

if __name__ == "__main__":
    unittest.main()
