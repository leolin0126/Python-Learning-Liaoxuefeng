# 模式匹配
# 例如，某个学生的成绩只能是A、B、C，用if语句编写
score = 'B'
if score == 'A':
    print('score is A.')
elif score == 'B':
    print('score is B.')
elif score == 'C':
    print('score is C.')
else:
    print('invalid score.')
# Python版本是V3.10或以上，可以用用match语句改写，则改写如下
# score = 'B'

# match score:
#     case 'A':
#         print('score is A.')
#     case 'B':
#         print('score is B.')
#     case 'C':
#         print('score is C.')
#     case _: # _表示匹配到其他任何情况
#         print('score is ???.')
# match语句除了可以匹配简单的单个值外，还可以匹配多个值、匹配一定范围，并且把匹配后的值绑定到变量
# age = 15

# match age:
#     case x if x < 10:
#         print(f'< 10 years old: {x}')
#     case 10:
#         print('10 years old.')
#     case 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18:
#         print('11~18 years old.')
#     case 19:
#         print('19 years old.')
#     case _:
#         print('not sure.')
# match语句匹配列表
# 我们假设用户输入了一个命令，用args = ['gcc', 'hello.c']存储，下面的代码演示了如何用match匹配来解析这个列表：
# args = ['gcc', 'hello.c', 'world.c']
# # args = ['clean']
# # args = ['gcc']

# match args:
#     # 如果仅出现gcc，报错:
#     case ['gcc']:
#         print('gcc: missing source file(s).')
#     # 出现gcc，且至少指定了一个文件:
#     case ['gcc', file1, *files]:
#         print('gcc compile: ' + file1 + ', ' + ', '.join(files))
#     # 仅出现clean:
#     case ['clean']:
#         print('clean')
#     case _:
#         print('invalid command.')





