def make_bank(balance):
    """Returns a bank function with a starting balance. Supports
    withdrawals and deposits.

    >>> bank = make_bank(100)
    >>> bank('withdraw', 40)    # 100 - 40
    60
    >>> bank('hello', 500)      # Invalid message passed in
    'Invalid message'
    >>> bank('deposit', 20)     # 60 + 20
    80
    >>> bank('withdraw', 90)    # 80 - 90; not enough money
    'Insufficient funds'
    >>> bank('deposit', 100)    # 80 + 100
    180
    >>> bank('goodbye', 0)      # Invalid message passed in
    'Invalid message'
    >>> bank('withdraw', 60)    # 180 - 60
    120
    """
    def bank(message, amount):
        "*** YOUR CODE HERE ***"
        nonlocal balance
        mess = ['deposit', 'withdraw']
        if message not in mess:
            return 'Invalid message'
        else:
            if message == mess[0]:
                balance = balance + amount
                return balance
            else:
                if amount > balance:
                    return 'Insufficient funds'
                else:
                    balance = balance - amount
                    return balance
    return bank

store = []

def make_withdraw(balance, password):
    """Return a password-protected withdraw function.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> error = w(90, 'hax0r')
    >>> error
    'Insufficient funds'
    >>> error = w(25, 'hwat')
    >>> error
    'Incorrect password'
    >>> new_bal = w(25, 'hax0r')
    >>> new_bal
    50
    >>> w(75, 'a')
    'Incorrect password'
    >>> w(10, 'hax0r')
    40
    >>> w(20, 'n00b')
    'Incorrect password'
    >>> w(10, 'hax0r')
    "Frozen account. Attempts: ['hwat', 'a', 'n00b']"
    >>> w(10, 'l33t')
    "Frozen account. Attempts: ['hwat', 'a', 'n00b']"
    >>> type(w(10, 'l33t')) == str
    True
    """
    "*** YOUR CODE HERE ***"
    def protected_bank(amount, pass_input):
        nonlocal balance
        if len(store) >= 3:
            return "Frozen account. Attempts: " + '[\'' + str(store[0]) + '\', \'' + str(store[1]) + '\', \'' + str(store[2]) + '\']'
        else:
            if pass_input != password:
                store.append(pass_input)
                return 'Incorrect password'
            else:
                if amount > balance:
                    return 'Insufficient funds'
                else:
                    balance = balance - amount
                    return balance
    return protected_bank

def count_nums(nums, dic):
    for num in nums:
        if dic.get(num):
            dic[num] += 1
        else:
            dic[num] = 1
    return dic

def repeated(t, k):
    """Return the first value in iterator T that appears K times in a row. Iterate through the items such that
    if the same iterator is passed into repeated twice, it continues in the second call at the point it left off
    in the first.

    >>> s = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> repeated(s, 2)
    9
    >>> s2 = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> repeated(s2, 3)
    8
    >>> s = iter([3, 2, 2, 2, 1, 2, 1, 4, 4, 5, 5, 5])
    >>> repeated(s, 3)
    2
    >>> repeated(s, 3)
    5
    >>> s2 = iter([4, 1, 6, 6, 7, 7, 8, 8, 2, 2, 2, 5])
    >>> repeated(s2, 3)
    2
    """
    assert k > 1
    "*** YOUR CODE HERE ***"
    nums, dic = [next(t) for _ in range(k)], {}
    dic = count_nums(nums, dic)
    while True:
        for num in nums:
            if dic[num] >= k:
                return num
        temp = nums.pop(0)
        if dic[temp] > 1:
            dic[temp] -= 1
        else:
            dic[temp] = 0
        num = next(t)
        nums.append(num)
        if dic.get(num):
            dic[num] += 1
        else:
            dic[num] = 1

def permutations(seq):
    """Generates all permutations of the given sequence. Each permutation is a
    list of the elements in SEQ in a different order. The permutations may be
    yielded in any order.

    >>> perms = permutations([100])
    >>> type(perms)
    <class 'generator'>
    >>> next(perms)
    [100]
    >>> try: #this piece of code prints "No more permutations!" if calling next would cause an error
    ...     next(perms)
    ... except StopIteration:
    ...     print('No more permutations!')
    No more permutations!
    >>> sorted(permutations([1, 2, 3])) # Returns a sorted list containing elements of the generator
    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    >>> sorted(permutations((10, 20, 30)))
    [[10, 20, 30], [10, 30, 20], [20, 10, 30], [20, 30, 10], [30, 10, 20], [30, 20, 10]]
    >>> sorted(permutations("ab"))
    [['a', 'b'], ['b', 'a']]
    """
    "*** YOUR CODE HERE ***"
    if len(seq) <= 1:
        yield seq
    elif len(seq) == 2:
        yield [seq[0], seq[1]]
        yield [seq[1], seq[0]]
    else:
        for i in range(len(seq)):
            res = permutations(seq[:i]+seq[i+1:])
            for result in res:
                yield [seq[i]] + result


def make_joint(withdraw, old_pass, new_pass):
    """Return a password-protected withdraw function that has joint access to
    the balance of withdraw.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> make_joint(w, 'my', 'secret')
    'Incorrect password'
    >>> j = make_joint(w, 'hax0r', 'secret')
    >>> w(25, 'secret')
    'Incorrect password'
    >>> j(25, 'secret')
    50
    >>> j(25, 'hax0r')
    25
    >>> j(100, 'secret')
    'Insufficient funds'

    >>> j2 = make_joint(j, 'secret', 'code')
    >>> j2(5, 'code')
    20
    >>> j2(5, 'secret')
    15
    >>> j2(5, 'hax0r')
    10

    >>> j2(25, 'password')
    'Incorrect password'
    >>> j2(5, 'secret')
    "Frozen account. Attempts: ['my', 'secret', 'password']"
    >>> j(5, 'secret')
    "Frozen account. Attempts: ['my', 'secret', 'password']"
    >>> w(5, 'hax0r')
    "Frozen account. Attempts: ['my', 'secret', 'password']"
    >>> make_joint(w, 'hax0r', 'hello')
    "Frozen account. Attempts: ['my', 'secret', 'password']"
    """
    "*** YOUR CODE HERE ***"
    temp = withdraw(0, old_pass)
    if type(temp) == str:
        if len(store) >= 3:
            return "Frozen account. Attempts: " + '[\'' + store[0] + '\', ' + '\'' +store[1] + '\', ' + '\'' + store[2] + '\']'
        return 'Incorrect password'
    else:
        def protected_bank_1(amount, pass_input_1):
            if len(store) >= 3:
                return "Frozen account. Attempts: " + '[\'' + store[0] + '\', ' + '\'' +store[1] + '\', ' + '\'' + store[2] + '\']'
            else:
                if pass_input_1 != old_pass and pass_input_1 != new_pass:
                    temp = withdraw(amount, pass_input_1)
                    if type(temp) == str:
                        store.append(pass_input_1)
                        return 'Incorrect password'
                    else:
                        return temp
                else:
                    return withdraw(amount, old_pass)
        return protected_bank_1


def remainders_generator(m):
    """
    Yields m generators. The ith yielded generator yields natural numbers whose
    remainder is i when divided by m.

    >>> import types
    >>> [isinstance(gen, types.GeneratorType) for gen in remainders_generator(5)]
    [True, True, True, True, True]
    >>> remainders_four = remainders_generator(4)
    >>> for i in range(4):
    ...     print("First 3 natural numbers with remainder {0} when divided by 4:".format(i))
    ...     gen = next(remainders_four)
    ...     for _ in range(3):
    ...         print(next(gen))
    First 3 natural numbers with remainder 0 when divided by 4:
    4
    8
    12
    First 3 natural numbers with remainder 1 when divided by 4:
    1
    5
    9
    First 3 natural numbers with remainder 2 when divided by 4:
    2
    6
    10
    First 3 natural numbers with remainder 3 when divided by 4:
    3
    7
    11
    """
    "*** YOUR CODE HERE ***"
    def remainder_back(num, k):
        # for j in range(1, 100):
        #     if j % num == k:
        #         yield j
        yield from [j for j in range(1, 20) if j % num == k]
    yield from [remainder_back(m, i) for i in range(m)]


def naturals():
    """A generator function that yields the infinite sequence of natural
    numbers, starting at 1.

    >>> m = naturals()
    >>> type(m)
    <class 'generator'>
    >>> [next(m) for _ in range(10)]
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    i = 1
    while True:
        yield i
        i += 1
