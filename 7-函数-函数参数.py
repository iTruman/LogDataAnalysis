# !usr/bin/python

# 把参数的名字和位置确定下来，就可以完成函数接口的定义了

# --------------------------------位置参数-------------------------------------

import math  # 引用math包

# 计算X平方的函数


def power(x):
    return x * x

# 调用：
print(power(3))  # 传入一个参数既可

# 但是计算X的3、4、5次方怎么办，如下：


def power(x, n):
    s = 1
    while n > 0:
        n -= 1
        s *= x
    return s

# 调用
print(power(2, 5))  # x和n，这两个参数都是位置参数，调用函数时，传入的两个值按照位置顺序依次赋给参数x和n。

# ----------------------------------默认参数-------------------！！！默认参数必须指向不变参数

# 如果经常计算X的2（3）次方，可以把第二个参数的默认值设定为2（3）：
def power(x, n = 2):
    s = 1
    while n > 0:
        n -= 1
        s *= x
    return s

# 调用
print(power(5))  # 当调用power(5)时，就相当于调用power(5, 2),  不是n=2的情况就要明确传入 n 的值

# 必选参数在前，默选参数在后；当有多个参数时，变化大的参数在前，变化小的在后，变化最小的可以作为默认参数

# 小学生注册的函数


def enroll(name, gender, age=6, city='Beijing'):
    print('name', name)
    print('gender', gender)
    print('age', age)
    print('city', city)

# 调用
enroll('刘雨萌', 'F')                # 默认值相同只需要提供两个必要的参数
enroll('刘虞梦', 'F', 7)             # 与默认参数不同的需要提供额外的信息
enroll('Adam', 'M', city='Tianjin')  # 不按顺序提供部分默认参数时，需要把参数名写上；本调用的意思是，city参数用传进去的值，其他默认参数继续使用默认值。

# 默认参数的坑：先定义一个函数，传入一个list，添加一个end再返回


def add_end(L = []):
    L.append('end')
    return L

# 正常调用：
print(add_end([1, 2, 3]))
print(add_end(['x', 'y', 'z']))

# 默认调用：
print(add_end())  # 结果为：['end']
print(add_end())  # 结果为：['end', 'end']
print(add_end())  # 结果为：['end', 'end', 'end']    每调用一次，参数都在变化

# Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]
# 每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。

# 要修改上面的例子，我们可以用None这个不变对象来实现:


def add_end(L = None):
    if L is None:
        L = []
    L.append('end')
    return L

# 默认调用：
print(add_end())  # 结果为：['end']
print(add_end())  # 结果为：['end']
print(add_end())  # 结果为：['end']   多次调用也不会有问题

# ----------------------------------可变参数-------------------------传入的参数是可变的，1个-·-任意个


# 计算任意几个参数的平方和，由于参数个数不确定，我们首先想到可以把a，b，c……作为一个list或tuple传进来，这样，函数可以定义如下：
def cacl(numbers):
    sum = 0
    for n in numbers:
        sum += power(n,2)
    return sum

# 调用，但是调用的时候需要先构造一个list或者一个tuple出来,有点麻烦
print(cacl([1, 2, 3]))
print(cacl((1, 3, 5, 7)))

# -----------------------------可变参数定义函数-------------------------------


def cacul(*numbers):    # 加了一个*号，在函数内部，参数numbers接收到的是一个tuple，因此可以传入任意一个参数，包括0个参数
    sum = 0
    for i in numbers:
        sum += i * i
    return sum
# 调用
print(cacul(1,2,3))
print(cacul())

# 如果已经有一个list或者tuple，要调用一个可变参数怎么办
nums = [1, 2, 3]

S = cacul(nums[0], nums[1], nums[2])  # 这种调用方法可以，但是太麻烦
print(S)

# 可以在list或者tuple前面加一个*号，把list或tuple的元素变成可变参数传进去
S2 = cacul(*nums)    # *nums 表示把nums这个list的所有元素作为可变参数传进去，写法很常见，很有用
print(S2)

# ---------------------------关键字参数--------------------------------
# 关键字参数允许你传入0~任意个含参数名的参数，這额关键字参数在内部自动组装成为一个dict


def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('刘雨萌', 22)  # 只传入必选参数
person('刘玉猛', 22, city='北京')                # 传入任意个数的关键字参数，一个
person('刘玉猛', 22, city='北京', job='工程师')  # 传入任意个数的关键字参数，两个

# 看完也可以先组装出一个dict，然后把dict作为关键字参数传进去
extra = {'city':'beijing', 'job':'Engineer'}
person('Jack',23, city=extra['city'], job=extra['job'])  # 传入的写法比较麻烦
person('Jho', 24, **extra)    # 简易写法
# **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，但是kw只是获得的dict只是extra的一个拷贝，对kw的改动不会影响到函数外的extra

# ----------------------------------------命名关键字参数-------------------------------


def person(name, age, **kw):  # 检查是否有city和job参数
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)

person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456) # 但是调用的时候仍可以传入不受限制的关键字参数

# 如果限制关键字参数的名字，就可以使用命名关键字参数，如：只接收city和job作为关键字参数


def person(name, age, *, city, job): # 和关键字**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的的参数被视为关键字参数
    print(name, age, city, job)

person('Jack', 24, city='Beijing', job='Engineer')  # 调用方式


def person(name, age, *args, city, job): # 如果函数中已经有一个可变参数，后面的关键字参数就不再需要特殊分隔符*了
    print(name, age, args, city, job)

skills = ['eating','playing','studing']
person('Truman', 22, skills[0], city='beijing', job='Engineer')  # 关键字参数调用必须带上参数名

# 当关键字参数有默认值时，可以不传入


def person(name, age, *, city='Beijing', job):
    print(name, age, city, job)

person('Jack', 24, job='Engineer')  # city关键字参数已经有默认值，可以不传入

# ----------------------使用命名关键字参数时，没有可变参数就必须加一个*作为分隔符，如果缺少*，python将无法区分位置参数和命名关键字参数--------

# ---------------------组合参数----------------------------

# 在Python定义函数可以将5种参数组合使用，但是顺序必须是： 必选参数、 默认参数、 可变参数、 命名关键字参数、 关键字参数。


def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

f1(1, 2)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99, ext=None)

# 通过一个tuple和dict，你也可以调用上述函数：
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)

args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)

# 对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。

# *args是可变参数，args接收的是一个tuple；

# **kw是关键字参数，kw接收的是一个dict
