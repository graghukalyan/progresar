import sys
import os
import unittest
from unittest.mock import patch
import io

# Add the project root to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)
from app.services.network_service import send_invite
from app.models.user import User

class TestNetworkService(unittest.TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_send_invite(self, mock_stdout):
        user = User("Test User", "test@example.com")
        send_invite(user)
        self.assertEqual(mock_stdout.getvalue().strip(), "Sending invite to test@example.com")

if __name__ == "__main__":
    unittest.main()
