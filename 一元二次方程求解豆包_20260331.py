import math  # 按课程要求，只用 math，不用 cmath

def quadratic(a, b, c):
    # 1. 先算判别式
    delta = b ** 2 - 4 * a * c

    # 2. 三种情况判断
    if delta > 0:
        # 两个不同实数解
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return x1, x2

    elif delta == 0:
        # 两个相同实数解
        x = (-b) / (2 * a)
        return x, x  # 返回两个一样的值

    else:
        # 无实数解
        print("此方程无实数解")
        return None  # 没有解就返回空

# 调用函数
x1, x2 = quadratic(4, 8, 4)

# 输出结果（格式化保留2位小数）
print("方程的解为：%.2f, %.2f" % (x1, x2))