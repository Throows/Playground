from src import main

from unittest.mock import patch
from unittest import TestCase

class test_main(TestCase):

    @patch("builtins.input", return_value="1,3")
    def test_operation_input_separator(self, input):
        self.assertEqual(main.GetOperationInput(), 10, "Power or separator not working")

    @patch("builtins.input", return_value="3")
    def test_operation_input_single(self, input):
        self.assertEqual(main.GetOperationInput(), 8, "Power not working")

    @patch("builtins.input", return_value="5")
    def test_operation_input_all(self, input):
        self.assertEqual(main.GetOperationInput(), 30, "Power not working")
    
