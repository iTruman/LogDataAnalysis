# !usr/bin/python

# List Comprehensions 是Python内置的功能强大，可以创建list生成式

# 创建list[1,2,3,4,5,6,7,8,9,10],可以用list(range(1,11))
L = []
S = []
for x in range(1,11):
    L.append(x)           # 生成[1,2,3,4,5,6,7,8,9,10]
    S.append(x * x)       # 生成[1,4,9,16,25,36,49,64,81,100]

print(L)
print(S)

# 一句话代替上面的生成

T = [x for x in range(1,11)]
D = [x * x for x in range(1,11)]
D1 = [x * x for x in range(1,11) if x % 2 == 0]   # 仅选出偶数的平方
print(T)
print(D)
print(D1)

# 两层循环实现全排列
M = [m + n for m in 'abc' for n in '123']
print(M)

# 三层实现全排列 ----三层以上很少用
M1 = [m + n + i for m in 'abc' for n in '123' for i in '222']
print(M1)

# 列出当前目录下所有的文件和文件名：
import os
print([d for d in os.listdir('D:.')]) # D盘中的文件

# for循环可以使用两个甚至多个变量，比如dict的 iterms()可以同时迭代key和value

D = {'x':'A', 'y':'B', 'z':'C'}

for k,v in D.items():
    print(k,'=',v)

# 把一个字符串中的所有字母变成小写
L = ['Hello', 'World', 'Python', 'TEST']
print(L)
S = [s.lower() for s in L]
print(S)

# 如果遇到list中既有字符串又包含证书，用lower()则会报错，可以使用内置isinstance函数做一步判断

# 对L中的字符串转小写，跳过数字


def Tolower(st):
    if not isinstance(st, str):
        return str(st)
    else:
        return st
L1 = ['Hello', 'World', 'Python', 18, 'TEST', None]
L2 = []

for s in L1:
    s = Tolower(s)
    L2.append(s.lower())

# 只对str做转小写换换，其余仍旧保留
L3 = []
for i in L1:
    if not isinstance(i, str):
        L3.append(i)
    else:
        L3.append(i.lower())
print(L3)




