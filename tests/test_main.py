import unittest
from app.main import main
from unittest.mock import patch
import io

class TestMain(unittest.TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_main(self, mock_stdout):
        main()
        self.assertEqual(mock_stdout.getvalue().strip(), "Hello, World!")

if __name__ == "__main__":
    unittest.main()
