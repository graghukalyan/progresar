import sys
import os
import unittest
from unittest.mock import patch
import io

# Add the project root to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)
from app.main import main

class TestMain(unittest.TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_main(self, mock_stdout):
        main()
        self.assertEqual(mock_stdout.getvalue().strip(), "Welcome to Progresar!")

if __name__ == "__main__":
    unittest.main()
