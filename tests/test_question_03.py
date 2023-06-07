from tests.test_base import TestBase

class Test(TestBase):
   
    def test_01(self):
        input = str(1)
        expected_output = "2\n"
        self.input_output(input, expected_output)

    def test_02(self):
        __name__
        input = str(10)
        expected_output = "2,3,5,7,11,13,17,19,23,29\n"
        self.input_output(input, expected_output)

    def test_03(self):
        input = str(12)
        expected_output = "2,3,5,7,11,13,17,19,23,29,31,37\n"
        self.input_output(input, expected_output)

    def test_04(self):
        input = str(20)
        expected_output = "2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71\n"
        self.input_output(input, expected_output)
