import cmath

def quadratic(a, b, c):
    """
    求解一元二次方程 ax² + bx + c = 0 的两个解
    :param a: 二次项系数 (不能为0)
    :param b: 一次项系数
    :param c: 常数项
    :return: 方程的两个解（元组形式）
    """
    # 第一步：判断a是否为0，若为0则不是一元二次方程，抛出异常
    if a == 0:
        raise ValueError("参数a不能为0，否则不是一元二次方程！")
    
    # 第二步：计算判别式Δ
    delta = b ** 2 - 4 * a * c
    
    # 第三步：根据求根公式计算两个解
    sqrt_delta = cmath.sqrt(delta)
    x1 = (-b + sqrt_delta) / (2 * a)
    x2 = (-b - sqrt_delta) / (2 * a)
    
    # 返回两个解
    return x1, x2

# 👇 正确调用函数（缩进、语法都规范）
x1, x2 = quadratic(2, 15, 5)

# 👇 用格式化字符 % 保留2位小数（核心需求）
print("方程的解为：%.2f, %.2f" % (x1.real, x2.real))