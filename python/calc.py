
class Calc:
    def add(self,a,b):
        try:
            res = a + b
        except Exception as e:
            res = '参数类型错误'
        return res

    def div(self,a,b):
        try:
            res = a / b
        except ZeroDivisionError:
            res = '除数不能为0'
        except Exception:
            res = '参数类型错误'
        return res