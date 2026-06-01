# for...in循环。依次把list或tuple中的每个元素迭代出来
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)
# 比如我们想计算1-10的整数之和，可以用一个sum变量做累加
sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)
# 计算1-100的整数之和，先用range()函数（注意左闭右开区间）生成整数序列，再通过list()函数可以转换为list。
sum = 0
for x in range(101):
    sum = sum + x
print(sum)
# 计算1-10000的整数之和，先用range()函数（注意左闭右开区间）生成整数序列，再通过list()函数可以转换为list。
sum = 0
for x in range(10001):
    sum = sum + x
print(sum)
# 计算100以内所有奇数之和（使用for...in循环语句）
sum = 0
for x in range(1,100,2):
    sum = sum + x
print(sum)
# 计算100以内所有奇数之和（使用while循环语句）
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)
# 练习：利用循环依次对list中的每个名字打印出Hello, xxx!
# '格式串' % 变量，中间绝对不能加逗号
# 变量不要乱加引号：y 是变量，'y' 是字符串，完全两回事
# 括号要成对：print( 后面的内容，要保证括号完整闭合
L = ['Bart', 'Lisa', 'Adam']
for y in L:
    print('Hello, %s !' % y)
# 练习：利用循环依次对list中的每个名字打印出Hello, xxx!
L = ['Bart', 'Lisa', 'Adam']
for y in L:
    print(f'Hello, {y} !')
# 练习：利用循环依次对list中的每个名字打印出Hello, xxx!
L = ['Bart', 'Lisa', 'Adam']
for y in L:
    print('Hello, {0} !'.format(y))
# 如果要提前结束循环，可以用break语句
n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')
# 如果想跳过某些循环，可以用continue语句
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)




