from tests.test_base import TestBase

class Test(TestBase):
   
    def test_01(self):
        input = str(2)
        expected_output = "dois\n"
        self.input_output(input, expected_output)

    def test_02(self):
        __name__
        input = str(17)
        expected_output = "dezessete\n"
        self.input_output(input, expected_output)


    def test_03(self):
        __name__
        input = str(25)
        expected_output = "vinte e cinco\n"
        self.input_output(input, expected_output)

    def test_04(self):
        input = str(40)
        expected_output = "quarenta\n"
        self.input_output(input, expected_output)

    def test_05(self):
        input = str(89)
        expected_output = "oitenta e nove\n"
        self.input_output(input, expected_output)
