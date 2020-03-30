from python.calc import Calc
import pytest

add_data = [
    (1, 2, 3),
    (2, -3, -1),
    (3, -2, 1),
    (2, -2, 0),
    (-2, -1, -3),
    (0.0003, 0.002, 0.0023),
    (2, 0.01, 2.01),
    (-1, 0.01, -0.99),
    (999999, 888888, 1888887),
    (0, 1, 1),
    (0, -1, -1),
    (0, 0, 0)
]

div_data = [
    (2, 1, 2),
    (-2, -1, 2),
    (2, 3, 0.6666666666666666),
    (1, 0.25, 4),
    (0.25, 4, 0.0625),
    (-5, 8, -0.625),
    (0, 1, 0),
    (1, 0, 1),
    (0, 0, 1),
    (9999999,1111111,9)
]

class TestCalc:
    def setup(self):
        self.calc = Calc()

    '''
       1.正整数相加
       2.一正一负相加（结果为正，负，0）
       3.负数相加
       4.小数相加
       5.整数加小数（正负）
       6.大数相加
       7. 0和整数 （正负）
       8. 都为0
    '''
    @pytest.mark.parametrize("a,b,r",add_data)
    def test_add_1(self,a,b,r):
        assert self.calc.add(a, b) == r

    '''
        1.正整数相除
        2.负整数相除
        3.分子或分母为小数
        4.结果为正整数
        5.结果为小数
        6.结果负数
        7.分子为0
        8.分母为0
        9.两者都为0
        10. 大数
    '''
    @pytest.mark.parametrize(['a','b','r'],div_data)
    def test_div_1(self,a,b,r):
        if b == 0:
            with pytest.raises(ZeroDivisionError,match='除数不能为0'):
                raise ZeroDivisionError('除数不能为0')
        else:
            assert self.calc.div(a, b) == r

# if __name__ == '__main__':
#     pytest.main()

