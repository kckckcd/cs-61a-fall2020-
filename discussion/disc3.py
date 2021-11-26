"""
    Question 1.1
    递归函数练习
"""

def multiply(m, n):
    """
        使用递归实现乘法函数
        m, n为正整数
    """
    min_num = min(m, n)
    max_num = n if min_num == m else m
    if min_num == 1:
        return max_num
    else:
        return max_num + multiply(max_num, min_num-1)


# print(multiply(5, 3))

"""
    Question 1.3
    递归练习
"""

def hailstone(n, step=0):
    """
        使用递归改写hailstone函数
    """
    if n == 1:
        step += 1
        print(n)
        return step
    elif n % 2 == 0:
        step += 1
        print(n)
        step = hailstone(n//2, step)
        return step
    else:
        step += 1
        print(n)
        step = hailstone(n*3+1, step)
        return step

# a = hailstone(10)
# print(a)

"""
    Question 1.4
    将两个数字按照递减顺序结合
"""
def get_digit(num, i):
    """
        输出num从左到右的第i位
    >>> get_digit(1234, 0)
    4
    >>> get_digit(1234, 2)
    2
    """
    rest = num % (10**(i+1))
    if rest < 10:
        return rest
    else:
        return rest // (10**i)

def merge_short(num_long, num_short):
    """
        将num_long和num_short组合，return组合后的数字
        num_short只有一位
    """
    temp = 0
    while num_long // (10**temp):
        digit = get_digit(num_long, temp)
        if digit >= num_short:
            break
        temp += 1
    res = num_long % (10**temp)
    return (num_long-res)*10 + num_short*(10**temp) + res

def split(num):
    """
        返回num的末位数字和剩下的数字
    """
    return num // 10, num % 10

def merge(n1, n2):
    min_num = min(n1, n2)
    max_num = n1 if min_num == n2 else n2
    if min_num == 0:
        return max_num
    elif min_num < 10:
        return merge_short(max_num, min_num)
    else:
        rest, last = split(min_num)
        return merge(merge_short(max_num, last), rest)

# print(merge(31, 42))
# print(merge(21, 0))
# print(merge(21, 31))

"""
    Question 1.5
    递归练习
"""

def make_func_repeater(f, x):
    def repeat(n):
        if n ==  1:
            return f(x)
        else:
            return make_func_repeater(f, f(x))(n-1)
    return repeat

# incr_1 = make_func_repeater(lambda x: x + 1, 1)
# print(incr_1(2))
# print(incr_1(5))

"""
    Question 1.6
    用递归实现is_prime()
"""

def is_prime(n):
    def prime_helper(num, state):
        if num == 1 or num % state == 0:
            return False
        elif num == 2 or state > num // 2:
            return True
        else:
            return prime_helper(n, state+1)
    return prime_helper(n, 2)

# print(is_prime(7))
# print(is_prime(10))
# print(is_prime(1))
