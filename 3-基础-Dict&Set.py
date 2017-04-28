# !usr/bin/python

# Python内置的字典：dict, 全称：dictionary，在其他语言中也称为 map
# dict 使用 键-值 存储，具有极快的查找速度，如用Python写一个dict： 名字-成绩
d = {'Micheal': 95, 'Bob': 75, 'Tracy': 85}
print(d['Micheal'])  # 快速查找Micheal的成绩为95
print(d)  # dict的内部存放的顺序和key放入的顺序是没有关系的

# 添加dict元素, 通过Key-value添加，多次对一个key放入多个value前面的value会被后面的value冲掉
d['Adam'] = 67
print(d)
print(d['Adam'])

# 避免key不存在的错误，一是：可以通过in判断key是否存在
print('Tomas' in d)  # Tomas不存在字典d中，返回False
print('Adam' in d)   # Adam存在字典d中，返回True

# 二是：通过dict提供的get方法，如果key不存在，可以返回None，或者自己指定那个的Value
b = d.get('Tomas')     # 返回None
print(b)
c = d.get('Tomas',-1)  # 返回自己指定的value值：-1
print(c)

# 删除key，pop(key)方法
d.pop('Adam')
print(d)

# dict插入和查找快，但是占用大量内存，浪费内存，list恰好相反；
# dict中的key是不可变对象，list可变不能作为dict的key，key不可以相同，
# dict是采用空间来换取时间的一种方法


# set和dict类似，但是set不存储value，key也不相同,set中不存在重复的key
# 创建一set需要一个list作为输入集合：
s1 = set([1, 2, 3])
print(s1)

# 重复元素在set中会被过滤
s2 = set([1, 2, 3, 3, 3])
print(s2)

# 通过add(key)方法，添加元素到set中，可以重复添加但是不会有效果
s1.add(4)
print(s1)

s1.add(4)  # 重复添加，无效果
print(s1)

# remove(key)方法删除元素
s1.remove(3)
print(s1)

# set可以看成数学意义上的无序和无重复元素的集合，因此两个set可以做数学意义上的交集和并集

s3 = set([1, 2, 3])
s4 = set([2, 3, 4])
s5 = s3 & s4
s6 = s3 | s4
print('交集为:', s5, '并集为:', s6)

# str是不变对象，list是可变对象，对list进行操作，list的内容是会变化的，如：
a = ['c', 'b', 'a']
print(a)
a.sort()
print(a)   # list的内容已经发生变化

# 对不可变对象str，进行操作，str内容不会变化：
st = 'abc'
st.replace('a', 'A')
st1 = st.replace('a', 'A')
print(st)   # st没有发生变化
print(st1)  # st1有变化，replace()只是创建了一个新字符串返回给st1，st并没有变化

# 把tuple放入set中
s1 = set([1, (1, 2, 3), 3])
print(s1)
