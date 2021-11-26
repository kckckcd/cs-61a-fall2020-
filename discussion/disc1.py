""" discussion 01  kckcd
    date 2021/07/17 for a bright future"""

def wear_jacket_with_if(temp, raining):
    """
    >>> wear_jacket_with_if(90, False)
    False
    >>> wear_jacket_with_if(40, False)
    True
    >>> wear_jacket_with_if(100, True)
    True
    """
    """
    question 1.1
    version-1 normal version
    if temp < 60 or raining:
        return True
    return False
    """
    return temp < 60 or raining

"""
question 1.2
"""
def square(x):
    print("here!")
    return x * x

def so_slow(num):
    x = num
    while x > 0:
        x = x + 1
    return x / 0

# square(so_slow(5)) timeout

def is_prime(n):
    """
    evaluate n is a prime number or not:
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    """
    k = 2
    while k < n // 2:
        if n % k == 0:
            return False
        k += 1
    return True
