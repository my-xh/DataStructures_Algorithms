# -*- coding: utf-8 -*-

class Stack:
    """栈"""

    def __init__(self):
        self._items = []

    def is_empty(self):
        return self._items == []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def peek(self):
        return self._items[-1]

    def size(self):
        return len(self._items)


if __name__ == '__main__':
    s = Stack()
    print(s.is_empty())
    s.push(4)
    s.push('dog')
    print(s.peek())
    s.push(True)
    print(s.size())
    print(s.is_empty())
    s.push(8.4)
    print(s.pop())
    print(s.pop())
    print(s.size())
