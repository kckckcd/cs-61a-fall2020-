"""
    disc06
    date: 2021/09/14
"""

"""
    Question 1.1
    nonlocal 可变函数练习
"""
# def memory(n):
#     """
#     >>> f = memory(10)
#     >>> f(lambda x: x * 2)
#     20
#     >>> f(lambda x: x - 7)
#     13
#     >>> f(lambda x: x > 5)
#     True
#     """
#     def f(g):
#         nonlocal n
#         n = g(n)
#         return n
#     return f
#
# """
#     Question 2.3
#     字典练习
# """
# def group_by(s, fn):
#     """
#     >>> group_by([12, 23, 14, 45], lambda p: p // 10)
#     {1: [12, 14], 2: [23], 4: [45]}
#     >>> group_by(range(-3, 4), lambda x: x * x)
#     {9: [-3, 3], 4: [-2, 2], 1: [-1, 1], 0: [0]}
#     """
#     grouped = {}
#     for num in s:
#         key = fn(num)
#         if grouped.get(key):
#             grouped[key].append(num)
#         else:
#             grouped[key] = [num]
#     return grouped
#
# """
#     Question 2.4
#     列表练习
# """
# def counter(nums, elment):
#     res = 0
#     for num in nums:
#         if num == elment:
#             res = res + 1
#     return res
#
# def add_this_many(x, el, s):
#     """ Adds el to the end of s the number of times x occurs
#     in s.
#     >>> s = [1, 2, 4, 2, 1]
#     >>> add_this_many(1, 5, s)
#     >>> s
#     [1, 2, 4, 2, 1, 5, 5]
#     >>> add_this_many(2, 2, s)
#     >>> s
#     [1, 2, 4, 2, 1, 5, 5, 2, 2]
#     """
#     times = counter(s, x)
#     return s.extend([el]*times)

# """
#     Question 4.1
#     生成器练习
# """
# def filter(iterable, fn):
#     """
#     >>> is_even = lambda x: x % 2 == 0
#     >>> list(filter(range(5), is_even)) # a list of the values yielded from the call to filter
#     [0, 2, 4]
#     >>> all_odd = (2*y-1 for y in range(5))
#     >>> list(filter(all_odd, is_even))
#     []
#     >>> naturals = (n for n in range(1, 100))
#     >>> s = filter(naturals, is_even)
#     >>> next(s)
#     2
#     >>> next(s)
#     4
#     """
#     nums = [num for num in iterable if fn(num)]
#     yield from nums

"""
    Question 4.2
    生成器练习
"""
def merge(a, b):
    """
    >>> def sequence(start, step):
    ...     while True:
    ...         yield start
    ...         start += step
    >>> a = sequence(2, 3) # 2, 5, 8, 11, 14, ...
    >>> b = sequence(3, 2) # 3, 5, 7, 9, 11, 13, 15, ...
    >>> result = merge(a, b) # 2, 3, 5, 7, 8, 9, 11, 13, 14, 15
    >>> [next(result) for _ in range(10)]
    [2, 3, 5, 7, 8, 9, 11, 13, 14, 15]
    """
    """
        我这代码也太蠢了吧:(
    """
    while True:
        nums1 = [next(a) for _ in range(10)]
        nums2 = [next(b) for _ in range(10)]
        res = nums1 + nums2
        res = list(set(res))
        res.sort()
        yield from res
