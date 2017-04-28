# !usr/bin/python

# ---------------------------------------递归函数

# 计算 n! 函数定义


def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)

# 计算 6!
print(fact(7))

# 但是不能防止栈溢出，如计算1000!的时候会出现栈溢出的现象；可以用尾递归优化来防止栈溢出，尾递归实际上和循环是等价的


def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

print(fact(100))
print(fact_iter(100, 1))

# 尾递归调用时，如果做了优化，栈不会增长，因此，无论多少次调用也不会导致栈溢出。

# 遗憾的是，大多数编程语言没有针对尾递归做优化，Python解释器也没有做优化，所以，即使把上面的fact(n)函数改成尾递归方式，也会导致栈溢出

# 利用递归函数移动汉诺塔:


def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
        return
    move(n-1, a, c, b)
    print('move', a, '-->', c)
    move(n-1, b, a, c)

move(5, 'A', 'B', 'C')
