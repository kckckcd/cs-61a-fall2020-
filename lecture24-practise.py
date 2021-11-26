"""
    date: 2021/10/20
    using built-in functions & comprehensions
"""
def smallest_abs_value(nums):
    """
    >>> smallest_abs_value([-4, -3, -2, 3, 2, 4])
    [2, 4]
    >>> smallest_abs_value([1, 2, 3, 4, 5])
    [0]
    """
    """
        version 1.0
        min_abs_val = min([abs(num) for num in nums])
        return [i for i in range(len(nums)) if abs(nums[i]) == min_abs_val]
    """
    # version 2.0
    min_abs_val = min(map(abs, nums))
    return list(filter(lambda i: abs(nums[i]) == min_abs_val, range(0, len(nums))))

def largest_sum_of_adjacent_element(nums):
    """
    >>> largest_sum_of_adjacent_element([-4, -3, -2, 3, 2, 4])
    6
    >>> largest_sum_of_adjacent_element([-4, 3, -2, -3, 2, -4])
    1
    """
    """
        version 1.0
        a, b = nums[0:-1], nums[1:]
        return max([a[i] + b[i] for i in range(len(a))])
    """
    a, b = nums[0:-1], nums[1:]
    return max([i + j for i, j in zip(a, b)])

def dic_map_ele(nums):
    """
    >>> dic_map_ele([5, 8, 13, 21, 34, 55, 89])
    {1: [21], 3: [13], 4: [34], 5: [5, 55], 8: [8], 9: [89]}
    """
    return {d: [num for num in nums if num % 10 == d] for d in range(10) if any([n for n in nums if n % 10 == d])}

def element_equal_some_other(nums):
    """
    >>> element_equal_some_other([-4, -3, -2, 3, 2, 4])
    False
    >>> element_equal_some_other([4, 3, 2, 3, 2, 4])
    True
    """
    return min([sum([1 for num in nums if num == d]) for d in nums]) > 1

"""
    date: 2021/10/20
    Linked List Exercise
"""
class Link:
    def __init__(self, first, rest=None):
        self.first = first
        self.rest = rest

    def __repr__(self):
        return "Link({}, {})".format(self.first, self.rest)


def is_ordered_link(test_link):
    """
    >>> test_link = Link(1, Link(3, Link(4)))
    >>> test_link
    Link(1, Link(3, Link(4, None)))
    >>> is_ordered_link(test_link)
    True
    >>> test_link = Link(1, Link(4, Link(3)))
    >>> is_ordered_link(test_link)
    False
    """
    def helper(link, val=-1000):
        if not link:
            return True
        else:
            if link.first >= val:
                val = link.first
                return helper(link.rest, val)
            else:
                return False
    return helper(test_link)

def ordered_by_other_rule(test_link, f=abs):
    """
    >>> test_link = Link(1, Link(-3, Link(4)))
    >>> ordered_by_other_rule(test_link)
    True
    >>> ordered_by_other_rule(test_link, lambda x: x // 2 if x > 0 else abs(x))
    False
    """
    if not test_link.rest:
        return True
    else:
        pre, cur = test_link, test_link.rest
        while cur != None:
            if f(pre.first) > f(cur.first):
                return False
            else:
                pre, cur = cur, cur.rest
        return True

def combine_links(link1, link2):
    """
    >>> link1 = Link(1, Link(5))
    >>> link2 = Link(1, Link(4))
    >>> combine_links(link1, link2)
    Link(1, Link(1, Link(4, Link(5, None))))
    """
    if link1 == None:
        return link2
    elif link2 == None:
        return link1
    elif link1.first > link2.first:
        return Link(link2.first, combine_links(link1, link2.rest))
    else:
        return Link(link1.first, combine_links(link1.rest, link2))

def end_link(link1, link2, pre):
    temp1, link1 = link1, link1.rest
    temp1.rest = None
    pre.rest = temp1
    return combine_links_with_old_space(link1, link2)

def insert(link1, link2):
    pre, cur = link2, link2.rest
    if cur == None:
        # temp1, link1 = link1, link1.rest
        # temp1.rest = None
        # link2.rest = temp1
        # return combine_links_with_old_space(link1, link2)
        return end_link(link1, link2, pre)
    else:
        while link1.first > cur.first:
            pre, cur = cur, cur.rest
            if cur == None:
                return end_link(link1, link2, pre)
        temp1, link1 = link1, link1.rest
        temp1.rest = None
        pre.rest, temp1.rest = temp1, cur
        return combine_links_with_old_space(link1, link2)

def combine_links_with_old_space(link1, link2):
    """
    >>> link1 = Link(1, Link(5))
    >>> link2 = Link(1, Link(4))
    >>> link3 = Link(4, Link(9, Link(12)))
    >>> combine_links_with_old_space(link2, link3)
    Link(1, Link(4, Link(4, Link(9, Link(12, None)))))
    """
    if link1 == None:
        return link2
    elif link2 == None:
        return link1
    elif link1.first > link2.first:
        return insert(link1, link2)
    else:
        return insert(link2, link1)
