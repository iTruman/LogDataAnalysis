# !usr/bin/env python
# enconding = utf-8

# 创建一个generator,最简单的方法是把[]改成()
L = [x * x for x in range(5, 10)]  # 创建列表
print(L)

g = (x * x for x in range(5, 10))  # 创建生成器
print(next(g))  # 可以使用next()访问g的内容，一般不用

for i in g:   # 生成器中保存的是算法，因此上文中使用过next()之后就计算出了g的下一个元素的值，所以循环从36开始
    print('n in g is:', i)

# !!! 生成器保存的是算法，并不是已经计算好的内容


def fib(max):  # 函数生成 斐波拉契数列
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n+1
    return 'DONE'

fib(6)


def fib1(max):     # 一个generator，而不是普通函数
    n, a, b = 0, 0, 1
    while n < max:
        yield b           # 在函数中定义yield关键字，函数就成了一个generator，执行时遇到yield返回，再次执行则从yield语句出继续
        a, b = b, a + b
        n = n + 1
    return 'fib is DONE'

g1 = fib1(6)
# for i in g1:  # 该种迭代方式访问不到return后面的返回值
#     print(i)

while True:  # 要拿到return返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中
    try:
        x = next(g1)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break
