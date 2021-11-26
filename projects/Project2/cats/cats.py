"""Typing test implementation"""

from utils import lower, split, remove_punctuation, lines_from_file
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns true. If there are fewer than K such paragraphs, return
    the empty string.
    """
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    if k > len(paragraphs) - 1:
        return ''
    elif k == 0:
        for paragraph in paragraphs:
            if select(paragraph):
                return paragraph
        return ''
    else:
        for i in range(len(paragraphs)):
            if select(paragraphs[i]):
                return choose(paragraphs[:i]+paragraphs[i+1:], select, k-1)
        return ''
    # END PROBLEM 1

def check_if(w):
    if (w >= 'a' and w <= 'z') or (w >= 'A' and w <= 'Z'):
        return True
    else:
        return False

def dele(w):
    # 删除word中的标点符号
    l = list(w)
    return ''.join([x for x in l if (x >= 'a' and x <= 'z') or (x >= 'A' and x <= 'Z')])

def about(topic):
    """Return a select function that returns whether a paragraph contains one
    of the words in TOPIC.

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    def check(para):
        words = lower(para)
        # if not check_if(words[-1]):
        #     words_new = words[:-1]
        # else:
        #     words_new = words
        words = split(words)
        for word in words:
            word = dele(word)
            for w in topic:
                if w == word:
                    return True
        return False
    return check
    # END PROBLEM 2


def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    """
    typed_words = split(typed)
    reference_words = split(reference)
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    not_accura, len_typed, len_ref = 0, len(typed_words), len(reference_words)
    if not len_typed or not len_ref:
        return 0.0
    if len_typed > len_ref:
        not_accura += (len_typed - len_ref)
    for i in range(min(len_typed, len_ref)):
        if typed_words[i] != reference_words[i]:
            not_accura += 1
    return (1 - not_accura / len(typed_words)) * 100.0
    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string."""
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    length = len(typed)
    if length == 0:
        return 0.0
    else:
        return length / 5 / (elapsed / 60)
    # END PROBLEM 4


def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than LIMIT.
    """
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    if user_word in valid_words:
        return user_word
    else:
        min_dif = min([diff_function(user_word, valid, limit) for valid in valid_words])
        if min_dif <= limit:
            for word in valid_words:
                if diff_function(user_word, word, limit) == min_dif:
                    return word
        else:
            return user_word
    # END PROBLEM 5


def shifty_shifts(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.
    """
    # BEGIN PROBLEM 6
    # assert False, 'Remove this line'
    len_s, len_g = len(start), len(goal)
    total = abs(len_g - len_s)
    # for i in range(len_s):
    #     if len_s[i] != len_g[i]:
    #         total += 1
    #     if total > limit:
    #         return total
    def shifty_shifts_helper(start, goal, total):
        if total > limit:
            return total
        elif not start or not goal:
            return total
        else:
            if start[0] != goal[0]:
                total += 1
            return shifty_shifts_helper(start[1:], goal[1:], total)
    return shifty_shifts_helper(start, goal, total)
    # END PROBLEM 6


def pawssible_patches(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL."""
    # assert False, 'Remove this line'
    # len_s, len_g = len(start), len(goal)
    # if not start or not goal: # Fill in the condition
    #     # BEGIN
    #     "*** YOUR CODE HERE ***"
    #     return 1
    #     # END
    # elif len_s == 1: # Feel free to remove or add additional cases
    #     # BEGIN
    #     "*** YOUR CODE HERE ***"
    #     if len_g == 1:
    #         if goal == start:
    #             return 0
    #         else:
    #             return 1
    #     elif start in goal:
    #         return len_g - len_s
    #     else:
    #         return len_g
    #     # END
    # elif len_g == 1:
    #     if goal in start:
    #         return len_s - len_g
    #     else:
    #         return len_s
    # else:
    #     add_diff = pawssible_patches(goal[0]+start, goal, limit)
    #     remove_diff = pawssible_patches(start[1:], goal, limit)
    #     substitute_diff = pawssible_patches(goal[0]+start[1:], goal, limit)
    #     res = min(add_diff, remove_diff, substitute_diff)
    #     if res > limit:
    #         return limit + 1
    #     else:
    #         return res
        # BEGIN
    # "*** YOUR CODE HERE ***"
    """
        误打误撞的完成了，我还是不能彻底理解
    """
    def pawssible_patches_helper(start, goal, total):
        if total > limit:
            return limit + 1
        elif not start or not goal:
            if not start:
                return total + len(goal)
            else:
                return len(start) + total
        else:
            if start[0] == goal[0]:
                return pawssible_patches_helper(start[1:], goal[1:], total)
            else:
                add_diff = pawssible_patches_helper(goal[0]+start, goal, total+1)
                remove_diff = pawssible_patches_helper(start[1:], goal, total+1)
                substitute_diff = pawssible_patches_helper(goal[0]+start[1:], goal, total+1)
                return min(add_diff, remove_diff, substitute_diff)
    return pawssible_patches_helper(start, goal, 0)
        # END


def final_diff(start, goal, limit):
    """A diff function. If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function'


###########
# Phase 3 #
###########


def report_progress(typed, prompt, user_id, send):
    """Send a report of your id and progress so far to the multiplayer server."""
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    dic, progress = {}, 1.0
    dic['id'] = user_id
    dic['progress'] = 0.0
    if typed == prompt:
        dic['progress'] = progress
    elif typed == prompt[:len(typed)]:
        progress = len(typed)/len(prompt)
        dic['progress'] = progress
    else:
        for i in range(len(typed)):
            if typed[i] != prompt[i]:
                progress = i / len(prompt)
                dic['progress'] =  progress
                break
    send(dic)
    return progress
    # END PROBLEM 8


def fastest_words_report(times_per_player, words):
    """Return a text description of the fastest words typed by each player."""
    game = time_per_word(times_per_player, words)
    fastest = fastest_words(game)
    report = ''
    for i in range(len(fastest)):
        words = ','.join(fastest[i])
        report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
    return report


def time_per_word(times_per_player, words):
    """Given timing data, return a game data abstraction, which contains a list
    of words and the amount of time each player took to type each word.

    Arguments:
        times_per_player: A list of lists of timestamps including the time
                          the player started typing, followed by the time
                          the player finished typing each word.
        words: a list of words, in the order they are typed.
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    times = []
    for i in range(len(times_per_player)):
        time, time_i = [], times_per_player[i]
        for j in range(1, len(time_i)):
            time_ij, time_next = times_per_player[i][j], times_per_player[i][j-1]
            time.append(time_ij-time_next)
        times.append(time)
    return game(words, times)
    # END PROBLEM 9


def fastest_words(game):
    """Return a list of lists of which words each player typed fastest.

    Arguments:
        game: a game data abstraction as returned by time_per_word.
    Returns:
        a list of lists containing which words each player typed fastest
    """
    player_indices = range(len(all_times(game)))  # contains an *index* for each player
    word_indices = range(len(all_words(game)))    # contains an *index* for each word
    # BEGIN PROBLEM 10
    "*** YOUR CODE HERE ***"
    store, res,  times = [], [], all_times(game)
    for player in player_indices:
        temp = []
        res.append(temp)
    for word in word_indices:
        player_min = min(player_indices, key = lambda player: times[player][word])
        store.append(player_min)
    for i in word_indices:
        word = word_at(game, i)
        res[store[i]] += [word]
    return res

    # END PROBLEM 10


def game(words, times):
    """A data abstraction containing all words typed and their times."""
    assert all([type(w) == str for w in words]), 'words should be a list of strings'
    assert all([type(t) == list for t in times]), 'times should be a list of lists'
    assert all([isinstance(i, (int, float)) for t in times for i in t]), 'times lists should contain numbers'
    assert all([len(t) == len(words) for t in times]), 'There should be one word per time.'
    return [words, times]


def word_at(game, word_index):
    """A selector function that gets the word with index word_index"""
    assert 0 <= word_index < len(game[0]), "word_index out of range of words"
    return game[0][word_index]


def all_words(game):
    """A selector function for all the words in the game"""
    return game[0]


def all_times(game):
    """A selector function for all typing times for all players"""
    return game[1]


def time(game, player_num, word_index):
    """A selector function for the time it took player_num to type the word at word_index"""
    assert word_index < len(game[0]), "word_index out of range of words"
    assert player_num < len(game[1]), "player_num out of range of players"
    return game[1][player_num][word_index]


def game_string(game):
    """A helper function that takes in a game object and returns a string representation of it"""
    return "game(%s, %s)" % (game[0], game[1])

enable_multiplayer = True  # Change to True when you're ready to race.

##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)
