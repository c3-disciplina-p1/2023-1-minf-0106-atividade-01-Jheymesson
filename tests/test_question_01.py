from tests.test_base import TestBase

class Test(TestBase):
   
    def test_01(self):
        input = "amor"
        expected_output = "Não é um palíndromo\n"
        self.input_output(input, expected_output)

    def test_02(self):
        input = "aibofobia"
        expected_output = "É um palíndromo\n"
        self.input_output(input, expected_output)

    def test_03(self):
        input = "mirim"
        expected_output = "É um palíndromo\n"
        self.input_output(input, expected_output)

    def test_04(self):
        input = "osso"
        expected_output = "É um palíndromo\n"
        self.input_output(input, expected_output)


    def test_05(self):
        input = "casa"
        expected_output = "Não é um palíndromo\n"
        self.input_output(input, expected_output)

  