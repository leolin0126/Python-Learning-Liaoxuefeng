# 使用dict和set
names = ['Michael', 'Bob', 'Tracy']
scores = [95, 75, 85]
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}

# 正确取值：从字典d中获取'Michael'的分数
print(d['Michael'])

# 也可以批量打印所有键值对
for name in names:
    print(f"{name} 的分数是：{d[name]}")

# 要避免key不存在的错误，有两种办法，一是通过in判断key是否存在
print('Thomas' in d)

# 二是通过dict提供的get()方法，如果key不存在，可以返回None,或者自己指定的value
print(d.get('Thomas'))

# 要删除一个key，用pop(key)方法，对应的value也会从dict中删除
print(d.pop('Bob'))
print(d)

# 要插入新的 key-value 对，直接写
# 语法：字典[新键名] = 对应的值
d['Adam'] = 99  # 插入新键 'Adam'，值为 99
print(d)

# 进阶写法：dict.update() 方法（批量插入 / 修改）
d = {'Michael': 95, 'Bob': 75}
# 批量插入/修改多个键值对，新增了 Tracy、Adam 两个键，把已有的 Michael 的值从 95 覆盖为 100
d.update({'Tracy': 85, 'Adam': 99, 'Michael': 100})
print(d)

# set和dict类似，也是一组key的集合，但不存储value。
s = {1, 2, 3}
print(s)

# 通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果
s.add(4)
print(s)

# 通过remove(key)方法可以删除元素
s.remove(4)
print(s)

# set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作
s1 = {1, 2, 3}
s2 = {2, 3, 4}
print(s1 & s2)
print(s1 | s2)

# 不可变对象,str是不变对象，而list是可变对象
a = ['c', 'b', 'a']
a.sort()
print(a)

b = 'abc'
b.replace('a', 'A')
print(b)

c = 'abc'
d = c.replace('a', 'A')
print(c)
print(d)


