"""
    disc05
    date: 2021/09/7
"""

def tree(label, branches=[]):
    return [label] + list(branches)

def branches(tree):
    return tree[1:]

def is_leef(tree):
    if branches(tree):
        return False
    else:
        return True

def label(tree):
    return tree[0]

def print_tree(t, indendt=0):
    print(' '*indendt + str(label(t)))
    for b in branches(t):
        print_tree(b, indendt+1)

"""
    Question 1.1
    递归练习，tree的深度
"""
def height(t):
    """
    >>> t = tree(3, [tree(5, [tree(1)]), tree(2)])
    >>> height(t)
    2
    """
    def height_helper(t, h=0):
        if is_leef(t):
            return h
        else:
            return max([height_helper(b, h+1) for b in branches(t)])
    return height_helper(t, 0)

"""
    Question 1.2
    递归练习，tree的最大值路径
"""
def max_path_sum(t):
    """
    >>> t = tree(1, [tree(5, [tree(1), tree(3)]), tree(10)])
    >>> max_path_sum(t)
    11
    """
    def max_path_sum_helper(t, max_sum=0):
        if is_leef(t):
            return max_sum + label(t)
        else:
            return max([max_path_sum_helper(b, label(t)) for b in branches(t)])
    return max_path_sum_helper(t)

"""
    Question 1.3
    递归练习，对tree的每个节点值进行平方操作
"""
def square_tree(t):
    """
    >>> numbers = tree(1, [tree(2, [tree(3), tree(4)]), tree(5, [tree(6, [tree(7)]), tree(8)])])
>>> print_tree(square_tree(numbers))
1
 4
  9
  16
 25
  36
   49
  64
    """
    if is_leef(t):
        return tree(label(t)**2, [])
    else:
        return tree(label(t)**2, [square_tree(b) for b in branches(t)])

"""
    Question 1.4
    递归练习，对tree的每个节点值进行平方操作
"""
def find_path(tree, x):
    """
    >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])] ), tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 10) # returns None
    """
    def find_path_helper(t, x, path):
        if is_leef(t):
            if label(t) == x:
                path.append(x)
                return path
            else:
                return []
        else:
            path.append(label(t))
            temp = []
            for b in branches(t):
                temp = find_path_helper(b, x, path) + temp
            return temp
    res = find_path_helper(tree, x, [])
    return res if res != [] else None

"""
    Question 2.2
    递归练习，输出不符合要求的tree的路径
"""
def prune_binary(t, nums):
    """
    >>> t = tree('1', [tree('0', [tree('0'), tree('1')]), tree('1', [tree('0')])])
    >>> t_new = prune_binary(t,  ['01', '110', '100'])
    >>> print_tree(t_new)
    '1'
     '0'
      '0'
     '1'
      '0'
    """
    if label(t) not in [num[0] for num in nums]:
        if is_leef(t) and label(t) == nums[0]:
            return t
        return None
    else:
        next_valid_nums = [num[1:] for num in nums]
        new_branches = []
        for b in branches(t):
            pruned_branch = prune_binary(b, next_valid_nums)
            if pruned_branch is not None:
                new_branches = new_branches + [pruned_branch]
        if not new_branches:
            return None
        return new_branches
