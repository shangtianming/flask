import pytest


class MusicPlayer:
    # 定义类属性记录单例对象引用
    # instance = None

    def __new__(cls, *args, **kwargs):
        # 1. 判断类属性是否已经被赋值
        # if cls.instance is None:
        if not hasattr(cls,"instance"):
            cls.instance = super().__new__(cls)

        # 2. 返回类属性的单例引用
        return cls.instance

print(id(MusicPlayer(1)))
print(id(MusicPlayer(2)))

for i in dir(MusicPlayer):
    print(i)


if __name__ == '__main__':
    pytest.main()
