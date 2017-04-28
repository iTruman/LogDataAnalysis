#!/usr/bin/python  第一个Python程序

# 输出Hello，World！
print ("Hello,World!")

# 行与缩进 缩进不一致，会导致运行错误
if True:
    print("Answer")
    print("True")
else:
    print("Answer")
    print("False")

# 多行语句用\来实现
Total = 1 +\
        2 +\
        3
print(Total)

# 等待用户输入 输入和输出
print ("Hello,World!")
name = input("请输入姓名：")
print("Hello", name)
print("1024 * 768 =",1027*768)

# Python基础 Python对大小写很敏感
a = 100
if a >= 0:
    print(a)
else:
    print(-a)

a=input("请输入一个整数：")
a=int(a)
if a >= 0:
    print("你输入的是正数：", a)
else:
    print("你输入的是负数：", a)

# python的数据类型和变量
a, b, c, d = 20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d))

a = 123  # a是整数
print(a)
a = 'ABC' # a变为字符串
print(a)

# 同一行显示多条语句
import sys
x = 'runoob'; sys.stdout.write(x + '\n')

# 数值运算
print("加法：", 5 + 4)       # 加法
print("减法：", 4.3 - 2)     # 减法
print("乘法：", 3 * 7)       # 乘法
print("除法，得到一个小数：", 2 / 4)       # 除法，得到一个浮点数
print("除法，得到一个整数：", 2 // 4)      # 除法，得到一个整数
print("取余：", 17 % 3)      # 取余
print("乘方：", 2 ** 5)      # 乘方

#字符串处理
str = 'Runoob'
print(str)           # 输出字符串
print(str[0:-1])     # 输出第一个个到倒数第二个的所有字符
print(str[0])        # 输出字符串第一个字符
print(str[2:5])      # 输出从第三个开始到第五个的字符
print(str[2:])       # 输出从第三个开始的后的所有字符
print(str * 2)       # 输出字符串两次
print(str + "TEST")  # 连接字符串