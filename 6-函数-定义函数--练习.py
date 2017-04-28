# !usr/bin/python

# 自定义一个函数接收三个参数，返回一元二次方程ax2 + bx + c = 0的两个解

import math  # 引用math包


def quadratic(a, b, c):
    # if not isinstance(a, b, c, (int, float)):
    #   raise TypeError('bad')
    D = b * b - 4 * a * c
    if a == 0:
        if b == 0:
            if c == 0:
                return '任意解'
            else:
                return '无实数解'
        elif b != 0:
            if c == 0:
                x1 = x2 = 0
                return x1, x2
            else:
                x1 = x2 = -b / c
                return x1, x2
    elif D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        return x1, x2
    elif D == 0:
        x1 = -b / (2 * a)
        x2 = -b / (2 * a)
        return x1, x2
    else:
        return '无实数解'


# 调用函数

# 参数错误的调用 print('函数的解为：', quadratic('1', '2', '3'))
print('函数的解为：', quadratic(0, 0, 1))
print('函数的解为：', quadratic(0, 2, 1))
print('函数的解为：', quadratic(1, 2, 0))
print('函数的解为：', quadratic(8, 2, 1))
