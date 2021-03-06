# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
import re
from math import ceil


def donuts(count):
    """
    Given an int count of a number of donuts, return a string of the
    form 'Number of donuts: <count>', where <count> is the number
    passed in. However, if the count is 10 or more, then use the word
    'many' instead of the actual count.

    >>> donuts(4)
    'Number of donuts: 4'
    >>> donuts(9)
    'Number of donuts: 9'
    >>> donuts(10)
    'Number of donuts: many'
    >>> donuts(99)
    'Number of donuts: many'
    """
    if count < 10:
        print('Number of donuts: ', count)
    else:
        print('Number of donuts: many')


def both_ends(s):
    """
    Given a string s, return a string made of the first 2 and the last
    2 chars of the original string, so 'spring' yields 'spng'.
    However, if the string length is less than 2, return instead the
    empty string.

    >>> both_ends('spring')
    'spng'
    >>> both_ends('Hello')
    'Helo'
    >>> both_ends('a')
    ''
    >>> both_ends('xyz')
    'xyyz'
    """
    if len(s) < 2:
        print('')
    else:
        first_two = s[:2]
        last_two = s[-2:]
        string = first_two + last_two
        print(string)


def fix_start(s):
    """
    Given a string s, return a string where all occurences of its
    first char have been changed to '*', except do not change the
    first char itself. e.g. 'babble' yields 'ba**le' Assume that the
    string is length 1 or more.

    >>> fix_start('babble')
    'ba**le'
    >>> fix_start('aardvark')
    'a*rdv*rk'
    >>> fix_start('google')
    'goo*le'
    >>> fix_start('donut')
    'donut'
    """
    s_list = list(s)
    for i in range(1, len(s_list)):
        if s_list[0] == s_list[i]:
            s_list[i] = '*'

    s = "".join(s_list)

    print(s)

def mix_up(a, b):
    """
    Given strings a and b, return a single string with a and b
    separated by a space '<a> <b>', except swap the first 2 chars of
    each string. Assume a and b are length 2 or more.

    >>> mix_up('mix', 'pod')
    'pox mid'
    >>> mix_up('dog', 'dinner')
    'dig donner'
    >>> mix_up('gnash', 'sport')
    'spash gnort'
    >>> mix_up('pezzy', 'firm')
    'fizzy perm'
    """
    a_list = list(a)
    b_list = list(b)
    a_two = a_list[:2]
    b_two = b_list[:2]

    a_list = b_two + a_list[2:]
    b_list = a_two + b_list[2:]

    a = "".join(a_list)
    b = "".join(b_list)

    print(a + ' ' + b)



def verbing(s):
    """
    Given a string, if its length is at least 3, add 'ing' to its end.
    Unless it already ends in 'ing', in which case add 'ly' instead.
    If the string length is less than 3, leave it unchanged. Return
    the resulting string.

    >>> verbing('hail')
    'hailing'
    >>> verbing('swiming')
    'swimingly'
    >>> verbing('do')
    'do'
    """
    if len(s) < 3:
        print(s)
    else:
        if 'ing' in s:
            print(s + 'ly')
        else:
            print(s + 'ing')

def not_bad(s):
    """
    Given a string, find the first appearance of the substring 'not'
    and 'bad'. If the 'bad' follows the 'not', replace the whole
    'not'...'bad' substring with 'good'. Return the resulting string.
    So 'This dinner is not that bad!' yields: 'This dinner is
    good!'

    >>> not_bad('This movie is not so bad')
    'This movie is good'
    >>> not_bad('This dinner is not that bad!')
    'This dinner is good!'
    >>> not_bad('This tea is not hot')
    'This tea is not hot'
    >>> not_bad("It's bad yet not")
    "It's bad yet not"
    """
    s = re.sub(r"not\s.*\sbad", 'good', s, 1)

    print(s)



def front_back(a, b):
    """
    Consider dividing a string into two halves. If the length is even,
    the front and back halves are the same length. If the length is
    odd, we'll say that the extra char goes in the front half. e.g.
    'abcde', the front half is 'abc', the back half 'de'. Given 2
    strings, a and b, return a string of the form a-front + b-front +
    a-back + b-back

    >>> front_back('abcd', 'xy')
    'abxcdy'
    >>> front_back('abcde', 'xyz')
    'abcxydez'
    >>> front_back('Kitten', 'Donut')
    'KitDontenut'
    """
    a_len = ceil(len(a)/2)
    b_len = ceil(len(b)/2)

    a_front = a[:a_len]
    a_back = a[a_len:]

    b_front = b[:b_len]
    b_back = b[b_len:]

    print(a_front + b_front + a_back + b_back)

if __name__ == '__main__':
    donuts(5)
    donuts(10)

    both_ends('spring')
    both_ends('Hello')
    both_ends('xyz')
    both_ends('a')

    fix_start('aardvark')
    fix_start('google')
    fix_start('donut')

    mix_up('pezzy', 'firm')
    mix_up('dog', 'dinner')

    verbing('do')
    verbing('swiming')
    verbing('hail')

    not_bad('This movie is not so bad')
    not_bad("It's bad yet not")
    not_bad('This dinner is not that bad!')
    not_bad('This tea is not hot')

    front_back('Kitten', 'Donut')
    front_back('abcde', 'xyz')



