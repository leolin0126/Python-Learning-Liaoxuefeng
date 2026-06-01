import math

def quadratic(a, b, c):
    
    # 定义变量delta，并用if、elif、else判断delta大于0、等于0、小于0的情况
    delta = b**2 - 4 * a * c
    
    # 当delta大于0，方程有2个不相等的实数解x1和x2
    if delta>0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print("\n方程有两个不相等实数解，为：%.2f, %.2f" % (x1.real, x2.real))
        return x1, x2
    
    # 当delta小于0，x1=x2
    elif delta==0:
        x = (-b)/(2 * a)
        print("\n方程两个相等实数解，为：%.2f , %.2f" % (x, x))
        return(x, x)
    
    # 当delta小于0，直接输出'此方程无实数解'
    else:
        print('\n此方程无实数解')

# 调用函数，并输出结果
quadratic(2, 15, 5)
print("-"*20)
quadratic(1,2,1)
print("-"*20)
quadratic(1,1,1)
