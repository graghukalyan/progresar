import sys
import os
import unittest


# Add the project root to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)
from app.utils.helpers import format_email

class TestHelpers(unittest.TestCase):
    def test_format_email(self):
        self.assertEqual(format_email(" Test@Example.com "), "test@example.com")
        self.assertEqual(format_email("user@domain.com"), "user@domain.com")
        self.assertEqual(format_email(" USER@DOMAIN.COM "), "user@domain.com")

if __name__ == "__main__":
    unittest.main()
