print(ord('A'))  # ord函数获取字符'A'的整数表示，并输出结果
print(ord('中'))  # ord函数获取字符'中'的整数表示，并输出结果
print(chr(66))  # chr函数把编码66转换为对应的字符，并输出结果
print(chr(25991))  # chr函数把编码25991转换为对应的字符，并输出结果
print('ABC'.encode('ascii'))  # 通过encode方法，用ASCII编码字符串ABC，并输出结果
print('中文'.encode('utf-8'))  # 通过encode方法，用UTF-8编码字符串中文，并输出结果
print(b'ABC'.decode('ascii'))  # 通过decode方法，用ASCII解码bytes字符串，并输出结果
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))  # 通过decode方法，用UTF-8解码bytes字符串，并输出结果
print(len('ABC'))  # 用len函数计算字符串ABC的str字符数
print(len('中文'))  # 用len函数计算字符串中文的str字符数
print(len(b'ABC'))  # 用len函数计算字符串的bytes字节数
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))  # 用len函数计算字符串的bytes字节数
print('Hello, %s' % 'world')  # 格式化运算符%之，用字符串替换%s替换字符串'world'
print('Hi, %s, you have $%d.' % ('Michael', 1000000))  # 格式化运算符%之，用字符串替换%s替换字符串'Michael'，用整数替换%d替换整数1000000
print('%02d-%04d' % (3, 1))  # 格式化运算符%之，用整数替换%d替换整数3和1，并在整数前补0
print('%.2f' % 3.1415926)  # 格式化运算符%之，用浮点数替换%f，为浮点数3.1415926的输出保留两位小数
print('Age: %s. Gender: %s' % (25, 'Male'))  # 格式化运算符%之，当被替换的数据类型不确定时，常用字符串替换%s
print('growth rate: %d %%' % 7)  # 格式化运算符%之，用%%表示百分号%
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))  # 第二种格式化字符，format()，会用传入的参数依次替换字符串内的占位符
r = 2.5
s = 3.14*r**2
print(f'The area of a circle with radius {r} is {s:.2f}')  # 第三种格式化字符，f-string，和普通字符串不同之处在于，字符串如果包含{xxx}，就会以对应的变量替换
print('\n5.2字符串和编码 练习')
print('题目: 小明的成绩从去年的72分提升到了今年的85分, 请计算小明成绩提升的百分点, 并用字符串格式化显示出\'xx.x%\', 只保留小数点后1位')
print('\n1.格式化运算符%')
print('\n输入代码:')
print('''result = ((85-72)/72)*100\nprint(\'从72分提高到85分，小明的成绩提升了 %.1f %%\' % (result)''')
print('\n输出结果:')
result = ((85-72)/72)*100
print('从72分提高到85分，小明的成绩提升了 %.1f %%' % (result))
print('\n2.格式化运算符format()')
print('\n输入代码:')
print('''result = ((85-72)/72)*100\nprint(\'从{0}分提高到{1}分，小明的成绩提升了 {2:.3f} %\'.format('72','85',result))''')
print('\n输出结果:')
result = ((85-72)/72)*100
print('从{0}分提高到{1}分，小明的成绩提升了 {2:.3f} %'.format('72','85',result))
print('\n3.格式化运算符f-string')
print('\n输入代码:')
print('''a = 72\nb = 85\nresult = ((85-72)/72)*100\nprint(f\'从{a}分提高到{b}分，小明的成绩提升了 {result:.2f} %\')''')
print('\n输出结果:')
a = 72
b = 85
result = ((85-72)/72)*100
print(f'从{a}分提高到{b}分，小明的成绩提升了 {result:.2f} %')