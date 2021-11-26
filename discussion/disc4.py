"""
    disc04
    date: 2021/08/16
"""

"""
    Question 1.1
    递归练习，n级台阶
"""
def count_stairs_ways(n):
    if n <= 2:
        return n
    else:
        return count_stairs_ways(n-1) + count_stairs_ways(n-2)

"""
    Qustion 1.2
    进阶递归练习
"""
def count_k(n, k):
    """
        It's too hard, I can't figure it out!
    """
    res = 0
    def count_k_helper(n, k, res):
        if n <= 1:
            return 1
        elif k == 1:
            return 1
        else:
            while k:
                res += count_k_helper(n-k, k, res)
                k -= 1
            return res
    return count_k_helper(n, k, res)


# print(count_k(3, 3))
# print(count_k(4, 4))
# print(count_k(10, 3))
# print(count_k(300, 1))

"""
    Question 2.2
    列表解析式练习
"""
def even_weighted(s):
    return [s[i]*i for i in range(len(s)) if i % 2 == 0]

# print(even_weighted([1, 2, 3, 4, 5, 6]))

"""
    Question 2.3
    未知列表练习
"""
def product(l):
    if l == []:
        return 1
    elif len(l) == 1:
        return l[0]
    else:
        return l[0]*product(l[1:])

def max_product(s):
    nums_even = [s[i] for i in range(len(s)) if i % 2 == 0]
    nums_odds = [s[i] for i in range(len(s)) if i % 2 == 1]
    product_even = product(nums_even)
    product_odds = product(nums_odds)
    return product_even if product_even > product_odds else product_odds

print(max_product([10, 3, 1, 9, 2]))
print(max_product([5, 10, 5, 10, 5]))
print(max_product([]))
