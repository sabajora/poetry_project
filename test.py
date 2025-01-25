import unittest
from io import StringIO
from unittest.mock import patch
from test_file import print_message

class TestPrintMessage(unittest.TestCase):

    @patch("sys.stdout", new_callable=StringIO)
    def test_print_message(self, mock_stdout):
        print_message()
        self.assertEqual(mock_stdout.getvalue().strip(), "Hello, nFactorial!")

if __name__ == "__main__":
    unittest.main()

