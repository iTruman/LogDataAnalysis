#!usr/bin/python 条件判断&循环

# 条件判断
age = int(input('请输入年龄：'))  # 或者写： a = input('请输入年龄：')  age = int(s)
if age >= 18:
    print('Your age is', age)
    print('adult')
elif age >= 6:
    print('Your age is', age)
    print('teenager')
else:
    print('Your age is', age)
    print('kid')

# if判断条件还可以简写;  只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False
x = 10
if x:
    print('True')

# 循环

# for循环： for x in ···循环就是把每个元素代入变量x，然后执行缩进块的语句。
names = ['Micheal', 'Bob', 'Tracy']
for name in names:
    print(name)
# 计算1-10的整数之和
sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print('1-10整数之和为：', sum)

# range()函数可以生成一个整数序列，再通过list()函数可以转换为list，range(5)生成的就是从0开始小于5的整数
M = list(range(5))
print(M)

# range(101)可以生成0-100的整数序列，计算和如下：
s = 0
for x in range(101):
    s = s + x
print(s)

# while循环：满足条件就不断循环

# 计算100以内的所有奇数之和
su = 0
n = 99
while n > 0:
    su = su + n
    n = n - 2
print('100以内的奇数和为：', su)

# 或者可以这样：
S = 0
i = 1
while i < 100:
    S = S + i
    i += 2
print('100以内的奇数和为：', S)

# 使用break语句提前退出循环，如：
n = 1
while n <= 100:
    if n > 10:  # 当 n=11时，执行break语句
        break   # break语句结束当前循环
    print(n)
    n += 1
print('End ..')

# 使用continue语句提前结束本轮循环，并直接进入下一轮循环
n = 0
while n < 10:
    n += 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue   # continue语句会直接进入下一轮循环，后面的print()语句不会执行
    print(n)