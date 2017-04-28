#!usr/bin/python List和Tuple数据类型

# Python数据类型：有序列表list
classmates = ['Micheal','Bob','Tracy']
print(classmates)        # 输出列表classmates中的元素
print(len(classmates))   # 获取列表classmates的长度
print(classmates[0])     # 通过索引访问列表classmates的元素，最后一个元素的索引是len(classmates)-1,索引越界会报错
print(classmates[-1])    # 访问列表classmates的最后一个元素
print(classmates[len(classmates)-1])  # 访问列表classmates的最后一个元素

# 追加元素到list末尾
classmates.append('Adam')
print(classmates)

# 元素添加到指定位置，如添加到第2位（索引号为1）
classmates.insert(1,'Jack')
print(classmates)

# 删除list末尾元素
classmates.pop()
print(classmates)

# 删除指定位置的元素，其中i是索引位置
classmates.pop(1)
print(classmates)

# 把某个元素替换成别的元素，可以直接赋值给对应的索引位置
classmates[1] = 'Sarah'
print(classmates)

# list里面的数据类型可以不同
L = ['Apple', 123, True]
print(L)

# list中的元素也可以是另一个list
S = ['Python','Java',['asp','php'],'scheme']
len(S) # 长度为4
print(S)

# 也可以这么写,相当于二维数组，类似的还有三维、四维···
P = ['asp', 'php']
S = ['Python', 'Java', P, 'scheme']
print(S)

# 要拿到‘php’元素，可以写成P[1],或者S[2][1],此时即二维数组的元素访问方式
print(P[1])
print(S[2][1])

# 当list为空时，长度为0
L = []
print(len(L))

# Python数据类型：元组tuple(也是有序列表)，但是tuple一旦初始化就不能修改:不能删除和添加
T = ('Micheal', 'Bob', 'Tracy')
print(T)
print(T[1])

# 定义空的tuple
t = ()
print(t)
# 只有一个元素的tuple定义方法,注意与T = （1）的区别
T = ('Micheal',)
U = (1,)
print(T,U)

# “可变的” tuple   tuple的不变是指每个元素的指向不变，T中第三个元素始终指向一个list并没有改成别的list，而list中的元素是可变的
T = ('a','b',['A', 'B'])
print(T)
T[2][0] = 'X'
T[2][1] = 'Y'
print(T)
