"""
    Question 1.1
"""

def keep_ints(cond, n):
    for i in range(1, n+1):
        if cond(i):
            print(i)

"""
    Question 1.2
    函数柯里化练习
"""

def make_keeper(n):
    def decide(cond):
        for i in range(1, n+1):
            if cond(i):
                print(i)
    return decide

def is_even(x):
    return x % 2 == 0

# keep_ints(is_even, 5)
# make_keeper(5)(is_even)

"""
    Question 1.7
    函数的自我指向练习
"""

def print_delayed(x):
    def delay_print(y):
        print(x)
        return print_delayed(y)
    return delay_print

# f = print_delayed(1)
# f = f(2)
# f = f(3)
# f = f(4)(5)
# f('hi')

"""
    Quesiont 1.8
    函数的自我指向练习
"""

def print_n(n):
    def inner_print(x):
        if n <= 0:
            print('done')
        else:
            print(x)
        return print_n(n-1)
    return inner_print

f = print_n(2)
f = f('hi')
f = f('hello')
f = f('bye')
g = print_n(1)
g('first')('second')('third')
