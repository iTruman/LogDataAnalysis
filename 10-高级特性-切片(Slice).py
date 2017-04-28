# !usr/bin/python

# 取前三个元素
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']


print(L[0:3])   # 切片取法，L[0:3]表示：从索引0开始取，渠道索引为3为止，但是不包括3，即索引0,1,2

print(L[:3])    # 如果第一个为0,0 还可以省略

print(L[-2:])   # 类似的，既然Python支持L[-1]取倒数第一个元素，那么它同样支持倒数切片 倒数第一个元素的索引是 -1

# 先创建一个0 ~ 99 的数列

L = list(range(100))
print(L)

print(L[:10])        # 取前 10 个数

print(L[-10:])       # 取后 10 个数

print(L[10:20])      # 取前 11~20 个数

print(L[:10:2])      # 前10个数，每 2 个取一个

print(L[::5])        # 所有数，每 5 个取一个

print(L[:])          # 什么都不写，可以原样复制一个list

# tuple是一种list，tuple切片：

T = (L)
print(T)

print(T[:10])

# 字符串也是一种list，字符串切片：

S = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print(S[:3])           # 取前 3 个

print(S[::2])          # 全体字符，每 2 个取 1 个

print(S[::2].lower())  # 每2个转换成小写

print(S.lower())       # 大写转换成小写







