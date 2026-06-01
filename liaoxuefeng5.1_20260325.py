# 转义字符\
print('I\'m \"OK\"!')
# 其他转义字符。\n换行，\t制表符，\\表示字符\
print('I\'m learning\nPython.')
print('\\\n\\')
# 用'''...'''表示多行内容
print('''line 1
line 2
line 3''')
# 多行字符串还可以在前面加上r使用
print('''hello,\nworld''')  # 2行字符，\n表示换行，'''表示多行字符
print('''hello,\n  
world''')  # 3行字符，\n表示换行，'''表示多行字符
print(r'''hello,\n  
world''')  # 2行字符，用r使得\n不转义，'''表示多行字符
# 5.1数据类型和变量 练习
print('数据类型和变量 练习')
n = 123  # 定义变量n为整数123。
f = 456.789  # 定义变量f为浮点数（小数）456.789。
s1 = 'Hello, world'  #  定义变量s1为字符串'Hello, world'。
s2 = 'Hello, \'Adam\''  # 定义变量s2为字符串'Hello, 'Adam'',用\转义Adam前后的单引号。
s3 = r'Hello, "Bart"'  # 定义变量s3为字符串'Hello, "Bart"',用r使得双引号不转义。
s4 = r'''Hello, 
Bob!'''  # 定义变量s4，'''表示多行字符
print(n,f,s1,s2,s3,s4)  # 在一行内输出上述6个变量

print("\n=== 只有r ===")
s5 = '''Hello, Bob!'''
print(s5)
s6 = r'''Hello, Bob!'''
print(s6)

# 实验 1：没有 \
print("\n=== 没有反斜杠 ===")
print(r"Hello, Bob!")
print("Hello, Bob!")

# 实验 2：有 \n
print("\n=== 有 \\n ===")
print(r"Hello,\nBob!")
print("Hello,\nBob!")

# 实验 3：文件路径
print("\n=== 文件路径 ===")
print(r"C:\new\test.txt")
print("C:\new\test.txt")  # \t 会被当作制表符！