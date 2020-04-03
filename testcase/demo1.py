'''
Created on 2019.3.22
单例模式
@author: Aiwenl
'''

class Music:
    instance = None
    init_tag = False
    def __new__(cls,*args, **kwargs):
        if cls.instance is None:
            cls.instance = object.__new__(cls, *args, **kwargs)
            print("__new__")
        return cls.instance
    
    def __init__(self):
        if Music.init_tag is False:
            object.__init__(self)
            print("ok")
            Music.init_tag = True

    def get_b(self):
        pass

    def display(self):
        pass



class C:
    pass

class A(Music):
    def get_b(self):
        return B()

class B(Music):
    def display(self):
        print('aiwenl')



if __name__ == '__main__':
    m1 = Music()
    m2 = Music()
    print(m1)
    print(m2)
    a = ' [1,2,3] '
    print(len(a))
    print(len(a.strip()))
    print('*'*20)
    A().get_b().display()