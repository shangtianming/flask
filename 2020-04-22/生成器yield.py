l = [1, 2, 3, 4]
it = iter(l)  # 迭代器
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(next(it), "=====分割线=====")

def test():
    yield 1

print(type(test()))  # 只要使用了yield的函数，对象都是迭代器

def fibonacci(n):
    a, b, count = 0, 1, 0
    while True:
        if (count > n):
            return
        yield a  # 生成器yield，返回a
        a, b = b, a + b
        count += 1
        print("运行次数：", count)


f = fibonacci(10)  # f是一个迭代器，由生成器返回生成

print("迭代器返回值：", next(f))  # 运行到a结束，第一次不会打印count
print("--分割线--")
print("迭代器返回值：", next(f))  # 再调用一次，从上次运行位置开始。先打印count，再打印迭代器返回值
