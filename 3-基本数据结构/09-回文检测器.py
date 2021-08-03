# -*- coding: utf-8 -*-

from pythonds.basic import Deque


def palindrome_checker(s):
    deque = Deque()
    still_equal = True

    for ch in s:
        deque.add_rear(ch)

    while deque.size() > 1 and still_equal:
        front = deque.remove_front()
        rear = deque.remove_rear()
        if front != rear:
            still_equal = False

    return still_equal


if __name__ == '__main__':
    print(palindrome_checker("lsdkjfskf"))
    print(palindrome_checker("toot"))
