# """
#     date: 2021/10/21
#     链表&树&显示
# """
#
# """
#     链表初始化
# """
# class Link:
#     empty = ()
#     def __init__(self, first, rest=empty):
#         assert rest is Link.empty or isinstance(rest, Link)
#         self.first = first
#         self.rest = rest
#
#     def __repr__(self):
#         if self.rest:
#             rest_str = ', ' + repr(self.rest)
#         else:
#             rest_str = ''
#         return 'Link({0}{1})'.format(repr(self.first), rest_str)
#
#     def __str__(self):
#         string = '<'
#         while self.rest is not Link.empty:
#             string += str(self.first) + ' '
#             self = self.rest
#         return string + str(self.first) + '>'
#
# """
#     Question 2.1
#     链表练习
# """
# def sum_nums(lnk):
#     """
#     >>> a = Link(1, Link(6, Link(7)))
#     >>> sum_nums(a)
#     14
#     """
#     if lnk == Link.empty:
#         return 0
#     else:
#         return lnk.first + sum_nums(lnk.rest)
#
# """
#     Question 2.2
#     链表练习
# """
# def multiply_lnks(lst_of_lnks):
#     """
#     >>> a = Link(2, Link(3, Link(5)))
#     >>> b = Link(6, Link(4, Link(2)))
#     >>> c = Link(4, Link(1, Link(0, Link(2))))
#     >>> p = multiply_lnks([a, b, c])
#     >>> p.first
#     48
#     >>> p.rest.first
#     12
#     >>> p.rest.rest.rest is Link.empty
#     True
#     """
#     # Note: you might not need all lines in this skeleton code
#     res = 1
#     for i in range(len(lst_of_lnks)):
#         if lst_of_lnks[i] == Link.empty:
#             return Link.empty
#         res, lst_of_lnks[i] = res * lst_of_lnks[i].first, lst_of_lnks[i].rest
#     return Link(res, multiply_lnks(lst_of_lnks))
#
# """
#     Question 2.3
#     链表练习
# """
# def flip_two(lnk):
#     """
#     >>> one_lnk = Link(1)
#     >>> flip_two(one_lnk)
#     >>> one_lnk
#     Link(1)
#     >>> lnk = Link(1, Link(2, Link(3, Link(4, Link(5)))))
#     >>> flip_two(lnk)
#     >>> lnk
#     Link(2, Link(1, Link(4, Link(3, Link(5)))))
#     """
#     if lnk == Link.empty or lnk.rest == Link.empty:
#         return
#     else:
#         lnk.first, lnk.rest.first = lnk.rest.first, lnk.first
#         return flip_two(lnk.rest.rest)
#
# """
#     Question 2.4
#     链表练习
# """
# def filter_link(link, f):
#     """
#     >>> link = Link(1, Link(2, Link(3)))
#     >>> g = filter_link(link, lambda x: x % 2 == 0)
#     >>> next(g)
#     2
#     >>> list(filter_link(link, lambda x: x % 2 != 0))
#     [1, 3]
#     """
#     """
#         迭代版本
#         while link != Link.empty:
#             if f(link.first):
#                 yield link.first
#             link = link.rest
#     """
#     if link == Link.empty:
#         return
#     else:
#         if f(link.first):
#             yield link.first
#         yield from filter_link(link.rest, f)
#
class Tree:
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = branches

    def is_leaf(self):
        return not self.branches

    def __repr__(self):
        if self.is_leaf():
            temp = ""
        else:
            temp = ", {}".format(self.branches)
        return "Tree({}{})".format(self.label, temp)
#
#
# """
#     Question 3.1
#     tree练习
# """
# def helper(num):
#     return num if num % 2 == 0 else num + 1
#
# def make_even(t):
#     """
#     >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4), Tree(5)])
#     >>> make_even(t)
#     >>> t.label
#     2
#     >>> t.branches[0].branches[0].label
#     4
#     """
#     t.label = helper(t.label)
#     if t.is_leaf():
#         return
#     else:
#         for b in t.branches:
#             make_even(b)
#         return
#
# """
#     Question 3.2
#     tree练习
# """
# def square_tree(t):
#     """Mutates a Tree t by squaring all its elements.
#     >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4), Tree(5)])
#     >>> square_tree(t)
#     >>> t.branches[0].label
#     4
#     >>> t.branches[0].branches[0].label
#     9
#     """
#     t.label = t.label ** 2
#     if t.is_leaf():
#         return
#     else:
#         for b in t.branches:
#             square_tree(b)
#         return
#
# """
#     Question 3.3
#     tree练习
# """
# def find_paths(t, entry):
#     """
#     >>> tree_ex = Tree(2, [Tree(7, [Tree(3), Tree(6, [Tree(5), Tree(11)])]), Tree(1, [Tree(5)])])
#     >>> find_paths(tree_ex, 5)
#     [[2, 7, 6, 5], [2, 1, 5]]
#     >>> find_paths(tree_ex, 12)
#     []
#     """
#     paths = []
#     if t.is_leaf() and t.label != entry:
#         return []
#     elif t.label == entry:
#         return [[t.label]]
#     else:
#         for b in t.branches:
#             temp = find_paths(b, entry)
#             for lst in temp:
#                 lst = [t.label] + lst
#                 paths.append(lst)
#         return paths

"""
    Question 3.4
    tree练习
"""
def mul(a, b):
    return a * b

def combine_tree(t1, t2, combiner):
    """
    >>> a = Tree(1, [Tree(2, [Tree(3)])])
    >>> b = Tree(4, [Tree(5, [Tree(6)])])
    >>> combined = combine_tree(a, b, mul)
    >>> combined.label
    4
    >>> combined.branches[0].label
    10
    """
    if t1.is_leaf():
        return Tree(combiner(t1.label, t2.label))
    else:
        return Tree(combiner(t1.label, t2.label), [combine_tree(t1.branches[i], t2.branches[i], mul) for i in range(len(t1.branches))])


"""
    Question 3.5
    tree练习
"""
def alt_tree_map(t, map_fn, valid=True):
    """
    >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4)])
    >>> negate = lambda x: -x
    >>> alt_tree_map(t, negate)
    Tree(-1, [Tree(2, [Tree(-3)]), Tree(4)])
    """
    if valid:
        t.label = map_fn(t.label)
    valid = not valid
    if t.is_leaf():
        return Tree(t.label)
    else:
        return Tree(t.label, [alt_tree_map(b, map_fn, valid) for b in t.branches])
