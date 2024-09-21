import unittest
from app.models.user import User
from app.controllers.user_controller import create_user
from unittest.mock import patch

class TestUser(unittest.TestCase):
    def test_user_creation(self):
        user = User("John Doe", "john@example.com")
        self.assertEqual(user.name, "John Doe")
        self.assertEqual(user.email, "john@example.com")

    @patch('app.services.network_service.send_invite')
    def test_create_user(self, mock_send_invite):
        user = create_user("Jane Doe", "jane@example.com")
        self.assertEqual(user.name, "Jane Doe")
        self.assertEqual(user.email, "jane@example.com")
        mock_send_invite.assert_called_once_with(user)

if __name__ == "__main__":
    unittest.main()
