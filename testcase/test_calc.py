from python.calc import Calc
import pytest


class TestCalc:
    def setup(self):
        self.calc = Calc()

    def test_add_1(self):
        assert self.calc.add(1, 2) == 3

    def test_add_2(self):
        assert self.calc.add('a',1) == '参数类型错误'

    def test_div_1(self):
        assert self.calc.div(1, 5) == 0.2

    def test_div_2(self):
        assert self.calc.div(1,0) == '除数不能为0'

    def test_div_3(self):
        assert self.calc.div(1,'a') == '参数类型错误'

# if __name__ == '__main__':
#     pytest.main()
