import unittest
from app.services.network_service import send_invite
from app.models.user import User
from unittest.mock import patch
import io

class TestNetworkService(unittest.TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_send_invite(self, mock_stdout):
        user = User("Test User", "test@example.com")
        send_invite(user)
        self.assertEqual(mock_stdout.getvalue().strip(), "Sending invite to test@example.com")

if __name__ == "__main__":
    unittest.main()
