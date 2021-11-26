def num_eights(x):
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
    # if n <= 8:
    #     return n
    # else:
    #     return
    increase, num = True, 0
    for i in range(1, n+1):
        if increase:
            num += 1
            if num_eights(i) or i % 8 == 0:
                increase = False
        else:
            num -= 1
            if num_eights(i) or i % 8 == 0:
                increase = True
    return num

print(pingpong(80))
