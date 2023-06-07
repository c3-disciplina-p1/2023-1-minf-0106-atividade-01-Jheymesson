import unittest
import sys
from io import StringIO
import abc
import importlib

class TestBase(unittest.TestCase, abc.ABC):

    def main(self):
        module_name = f'src.{self.__class__.__module__.split("test_")[1]}'
        module = importlib.find_loader(module_name)
        if module:
            module.load_module()
        else:
            importlib.import_module(module_name)

    def input_output(self, input, expected_output):
        input = StringIO(input)
        actual_output = StringIO()
        sys.stdin = input
        sys.stdout = actual_output 
        self.main()
        self.assertEqual(actual_output.getvalue(), expected_output)

    def setUp(self) -> None:
        self.input = sys.stdin
        self.output = sys.stdout
        return super().setUp()

    def tearDown(self) -> None:
        sys.stdin = self.input
        sys.stdout = self.output
        return super().tearDown()

