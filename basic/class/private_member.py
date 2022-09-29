# 一些特殊的私有类成员函数 __xxx__

class Mymodel():
    """this is __doc__ ouput"""

    def __init__(self):
        self.member = None
        print('__init__ called')

    def __del__(self):
        print('__del__ called')

    def __call__(self, *args, **kwargs):
        print('__call__ called')

    def __str__(self):
        return 'printing me!'

    def __getitem__(self, key):
        print('__getitem__ called')

    def __setitem__(self, key, value):
        print('__setitem__ called')

    def __delitem__(self, key):
        print('__delitem__ called')

    def __getslice__(self, i, j):
        print('__getslice__ called')

    def __setslice__(self, i, j, sequence):
        print('__setslice__ called')

    def __delslice__(self, i, j):
        print('__delslice__ called')


if __name__ == '__main__':
    # __doc__
    print(Mymodel.__doc__)

    # __module__ 模块名
    # __class__  类名
    myobj = Mymodel()
    print(myobj.__module__)
    print(myobj.__class__)

    # __init__ 构造函数
    # __del__  析构函数
    myobj = Mymodel() # __init__ called
    del myobj # __del__ called
    # __del__ called

    # __call__ 对象括号调用
    myobj = Mymodel()
    myobj() # __call__ called
    # __del__ called

    # __dict__ 类和对象都可调用，输出类或对象成员
    print(Mymodel.__dict__) # 类成员
    myobj = Mymodel()
    print(myobj.__dict__) # 对象成员
    # __del__ called

    # __str__ 对象被打印（print）时调用
    print(myobj)

    # __setitem__
    myobj['key'] = 'value'
    # __getitem__
    result = myobj['key']
    # __delitem__
    del myobj['key']

    # __setslice__
    result = myobj[0:1]
    # __getslice__
    myobj[0:1] = [11,22,33,44]
    # __delslice__
    del myobj[0:1]

    
