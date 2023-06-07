from tests.test_base import TestBase

class Test(TestBase):
   
    def test_01(self):
        input = str(125)
        expected_output = "soma dos digitos = 8\n"
        self.input_output(input, expected_output)

    def test_02(self):
        __name__
        input = str(3563)
        expected_output = "soma dos digitos = 17\n"
        self.input_output(input, expected_output)

    def test_03(self):
        input = str(12345)
        expected_output = "soma dos digitos = 15\n"
        self.input_output(input, expected_output)

    def test_04(self):
        input = str(0)
        expected_output = "soma dos digitos = 0\n"
        self.input_output(input, expected_output)




        
