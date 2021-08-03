# -*- coding: utf-8 -*-

from pythonds.basic import Queue


def hot_potato(namelist, num):
    queue = Queue()
    for name in namelist:
        queue.enqueue(name)

    while queue.size() > 1:
        for _ in range(num):
            queue.enqueue(queue.dequeue())
        queue.dequeue()

    return queue.dequeue()


if __name__ == '__main__':
    namelist = ['Bill', 'David', 'Susan', 'Jane', 'Kent', 'Brad']
    print(hot_potato(namelist, 7))
