from tests.test_base import TestBase

class Test(TestBase):
   
    def test_01(self):
        input = str(2)
        expected_output = "2\n"
        self.input_output(input, expected_output)

    def test_02(self):
        __name__
        input = str(14)
        expected_output = "41\n"
        self.input_output(input, expected_output)

    def test_03(self):
        input = str(276)
        expected_output = "672\n"
        self.input_output(input, expected_output)

    def test_04(self):
        input = str(3984)
        expected_output = "4893\n"
        self.input_output(input, expected_output)

    def test_05(self):
        input = str(12345)
        expected_output = "54321\n"
        self.input_output(input, expected_output)