# 1.list是一种有序的集合
classmates = ['Micheal', 'Bob', 'Tracy']
print(classmates)
# 2.len函数获取list中元素的个数
print(len(classmates))
# 3.用索引来访问list中的元素，从[0]开始
print(classmates[0])
print(classmates[1])
print(classmates[2])
# 4.用append函数添加元素到list末尾
classmates.append('Adam')
print(classmates)
# 5.用insert函数添加元素到list的指定位置
classmates.insert(3, 'Jackie')
print(classmates)
# 6.用pop函数删除list末尾的元素
classmates.pop()
'Adam'
print(classmates)
# 7.用pop(i)函数删除指定位置的元素
classmates.pop(3)
'Jackie'
print(classmates)
# 8.把某个元素替换成别的元素，可以直接赋值给对应的索引位置
classmates[1] = 'Sarah'
print(classmates)
# 9.list中的元素也可能是别的list，组成二维、三维等多维数组
s = ['python', 'java', ['asp', 'php'], 'scheme']
print(s[2][1])
# 练习
print('\n请用索引取出下面list的指定元素:')
print('''L = [['Apple', 'Google', 'Microsoft'],['Java', 'Python', 'Ruby', 'PHP'],['Adam', 'Bart', 'Bob']]''')
print('\n打印Apple, Python, Bob三个元素')
# 练习开始
print('\n练习开始\n')
L = [['Apple', 'Google', 'Microsoft'],['Java', 'Python', 'Ruby', 'PHP'],['Adam', 'Bart', 'Bob']]
print(L)
print(L[0][0])
print(L[1][1])
print(L[2][2])