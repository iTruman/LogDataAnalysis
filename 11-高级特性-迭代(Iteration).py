# !usr/bin/python

# 给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）
# 在Python中，迭代是通过for ··· in 来完成的

# dict的key迭代  ---因为dict是无序的，所以迭代的结果也是无序的
D = {'a':1, 'b':2, 'c':3}
for key in D:
    print(key)

for k in D.keys():
    print(k)

# dict的value迭代  ---因为dict是无序的，所以迭代的结果也是无序的

for v in D.values():
    print(v)

# 判断一个对象是否为可迭代的------通过collection模块的iteration类型判断

from collections import Iterable  # 应该放在文件头部

print(isinstance('abc', Iterable))         # str是否可迭代
print(isinstance([1, 2, 3], Iterable))     # list是否可迭代
print(isinstance(123, Iterable))           # 整数是否可迭代 ，不可以

# 对list实现下标循环， Python内置的enumerate函数可以吧一个list变成 索引-元素 对，可以同时迭代索引和元素本身

for i, value in enumerate(['A', 'B', 'C']):
    print(i,value)

# 同时引入两个变量
L=[(1,2), (3,4), (5,6)]
for x, y in L:
    print(x, y)

