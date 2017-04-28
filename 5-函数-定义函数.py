# !/usr/bin/python

# 定义函数  定义一个函数使用def语句，依次写出： 函数名、括号、括号中的参数、冒号，然后再缩进块中邪函数体，函数的返回值用return语句返回


# 自定义求绝对值函数 my_abs:
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
# 调用my_abs
a = -3
print(my_abs(a))

# 函数体内部的语句在执行时，一旦执行到return时，函数就执行完毕并将结果返回。如果没有return，函数执行完后也会返回，只是结果为None return None也可以写成return


# 定义一个什么也不做的空函数可以用pass语句：
def nop():
    pass  # pass语句可以用来做占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码先能运行起来

# pass也可以写在其他语句里，如：
age = int(input('请输入年龄：'))
if age >= 18:
    pass   # 什么也不做
else:
    print('You are still teenager ..')

# 参数检查
def my_abs1(x):
    if not isinstance(x, (int, float)):  # 对输入的参数进行检查，当类型不对是抛出错误
        raise TypeError('参数类型不对')
    if x >= 0:
        return x
    else:
        return -x
# 调用my_abs1
# print(my_abs1('2'))  # 参数类型不对，抛出错误
print(my_abs1(-3))   # 正常调用

# 返回多个值，如：

import math   # 导入math包，允许后续代码使用math包里的函数，如：sin cos  ---注意--- 导入包应该在文件头部导入


# 计算坐标的函数
def move(x, y, step, angle = 0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny
# 调用
x, y = move(100, 100, 60, math.pi/6)
print(x, y)           # 或者：print(move(100, 100, 60, math.pi/6))

# python返回值仍是单一值，本质为一个tuple，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值。


