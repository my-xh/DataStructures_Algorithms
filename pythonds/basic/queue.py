# -*- coding: utf-8 -*-

class Queue:
    """队列"""

    def __init__(self):
        self._items = []

    def is_empty(self):
        return self._items == []

    def enqueue(self, item):
        self._items.insert(0, item)

    def dequeue(self):
        return self._items.pop()

    def size(self):
        return len(self._items)


class Deque(Queue):
    """双端队列"""

    def add_front(self, item):
        self._items.append(item)

    def add_rear(self, item):
        super().enqueue(item)

    def remove_front(self):
        return super().dequeue()

    def remove_rear(self):
        return self._items.pop(0)


if __name__ == '__main__':
    q = Queue()
    print(q.is_empty())
    q.enqueue('dog')
    q.enqueue(4)
    q.enqueue(True)
    print(q.size())
    print(q.is_empty())
    q.enqueue(8.4)
    print(q.dequeue())
    print(q.dequeue())
    print(q.size())

    print('*' * 50)

    d = Deque()
    print(d.is_empty())
    d.add_rear(4)
    d.add_rear('dog')
    d.add_front('cat')
    d.add_front(True)
    print(d.size())
    print(d.is_empty())
    d.add_rear(8.4)
    print(d.remove_rear())
    print(d.remove_front())
