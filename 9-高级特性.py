# !usr/bin/python

# 构造一个1~99的奇数列表，可以通过循环实现

L = []
n= 1
while n <= 99:
    L.append(n)
    n += 2
print(L)

# 用函数调的形式来解决


def odd(n):
    L = []; i = 1
    if n == 1:
        L.append(1)
        return L
    else:
        while i <= n:
            L.append(i)
            i +=2
        return L

print(odd(1))
print(odd(10))
