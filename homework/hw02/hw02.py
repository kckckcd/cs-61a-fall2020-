HW_SOURCE_FILE=__file__


def num_eights(x):
    """Returns the number of times 8 appears as a digit of x.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    if not x :
        return 0
    else:
        if x % 10 == 8:
            return num_eights(x//10) + 1
        else:
            return num_eights(x//10)

def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(8)
    8
    >>> pingpong(10)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    -2
    >>> pingpong(30)
    -2
    >>> pingpong(68)
    0
    >>> pingpong(69)
    -1
    >>> pingpong(80)
    0
    >>> pingpong(81)
    1
    >>> pingpong(82)
    0
    >>> pingpong(100)
    -6
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    def pingpong_helper(index, dir, num):
        if index == n:
            return num
        else:
            if num_eights(index) or index % 8 == 0:
                if dir == 1:
                    return pingpong_helper(index+1, -1, num-1)
                else:
                    return pingpong_helper(index+1, 1, num+1)
            else:
                return pingpong_helper(index+1, dir, num+dir)
    return pingpong_helper(1, 1, 1)

def split(num):
    num %= 100
    return num % 10, num // 10

def missing_digits(n):
    """Given a number a that is in sorted, increasing order,
    return the number of missing digits in n. A missing digit is
    a number between the first and last digit of a that is not in n.
    >>> missing_digits(1248) # 3, 5, 6, 7
    4
    >>> missing_digits(1122) # No missing numbers
    0
    >>> missing_digits(123456) # No missing numbers
    0
    >>> missing_digits(3558) # 4, 6, 7
    3
    >>> missing_digits(35578) # 4, 6
    2
    >>> missing_digits(12456) # 3
    1
    >>> missing_digits(16789) # 2, 3, 4, 5
    4
    >>> missing_digits(19) # 2, 3, 4, 5, 6, 7, 8
    7
    >>> missing_digits(4) # No missing numbers between 4 and 4
    0
    >>> from construct_check import check
    >>> # ban while or for loops
    >>> check(HW_SOURCE_FILE, 'missing_digits', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n < 10:
        return 0
    elif n < 100:
        last, last_secend =  split(n)
        return last - last_secend - 1 if last > last_secend else 0
    else:
        last, last_secend = split(n)
        rest = last - last_secend - 1 if last > last_secend else 0
        return rest + missing_digits(n//10)


def next_largest_coin(coin):
    """Return the next coin.
    >>> next_largest_coin(1)
    5
    >>> next_largest_coin(5)
    10
    >>> next_largest_coin(10)
    25
    >>> next_largest_coin(2) # Other values return None
    """
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25

def next_smallest_coin(coin):
    if coin == 25:
        return 10
    elif coin == 10:
        return 5
    elif coin == 5:
        return 1

def find_near(num):
    if num >= 25:
        return 25
    elif num >= 10:
        return 10
    elif num >= 5:
        return 5
    else:
        return 1

def count_coins(total):
    """Return the number of ways to make change for total using coins of value of 1, 5, 10, 25.
    >>> count_coins(15)
    6
    >>> count_coins(10)
    4
    >>> count_coins(20)
    9
    >>> count_coins(100) # How many ways to make change for a dollar?
    242
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_coins', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    """
        搞不懂，真的搞不懂，莫名奇妙就通过了
    """
    coin_near = find_near(total)
    def count_coins_helper(target, max_coin):
        if max_coin == 1:
            return 1
        elif target == 0:
            return 1
        elif target == 1:
            return 1
        else:
            return count_coins_helper(target-max_coin, min(max_coin, target - max_coin)) + count_coins_helper(target, next_smallest_coin(max_coin))
    return count_coins_helper(total, coin_near)


from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> # ban any assignments or recursion
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    """
        amazing thoughts!!!
        i copy it from https://github.com/rigelJ/CS61A/blob/master/Homeworks/hw02/hw02.py
    """
    return lambda n:(lambda f:f(n,f))(lambda n,f:1 if n==1 else n*f(n-1,f))
