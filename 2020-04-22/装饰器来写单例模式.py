def single(cls):
    _instance={}
    def aa(*arg,**kwargs):
        if cls not in _instance:
            _instance[cls]=cls(*arg,**kwargs)
        print('========',_instance)
        return _instance[cls]
    return aa

@single
class A(object):
    a = 1

    def __init__(self, x=0):
        self.x = x
        print('这是A的类的初始化方法')


a1 = A(2)
a2 = A(3)
print(id(a1), id(a2))