# -*- coding: utf-8 -*-

from pythonds.priority_queue.task import Task
from pythonds.trees import BinaryHeap, BinarySearchTree


class PriorityQueue:
    """
    优先级队列
    PriorityQueue[ (key, priority), ... ]

    key: 元素唯一标识

    priority: 元素优先级，越小则优先级越高
    """

    def __init__(self):
        self.__heap = BinaryHeap()
        self.__tasks = BinarySearchTree()

    def __contains__(self, key):
        return self.__tasks.get(key) is not None

    def is_empty(self):
        return self.__heap.is_empty()

    def get_first_task(self):
        task: Task = self.__heap.find_min()
        if task:
            return task.key

    def enqueue(self, key, priority):
        if key in self.__tasks:
            raise ValueError(f'{key} already in queue')
        self.__tasks[key] = Task(key, priority)
        self.__heap.push(self.__tasks[key])

    def dequeue(self):
        task: Task = self.__heap.pop()
        del self.__tasks[task.key]
        return task.key

    def update_priority(self, key, priority):
        task: Task = self.__tasks.get(key)
        if task is None:
            return

        idx = self.__heap.index(task)
        if idx != -1:
            self.__tasks[key] = Task(key, priority)
            self.__heap.replace(idx, self.__tasks[key])

    def build_queue(self, arr: list):
        task_list = []
        for key, priority in arr:
            self.__tasks[key] = Task(key, priority)
            task_list.append(self.__tasks[key])
        self.__heap.build_heap(task_list)


if __name__ == '__main__':
    queue = PriorityQueue()
    print(f'当前队列为空：{queue.is_empty()}')
    queue.enqueue('a', 3)
    print('添加任务a, 优先级: 3')
    queue.enqueue('b', 1)
    print('添加任务b, 优先级: 1')
    queue.enqueue('c', 2)
    print('添加任务c, 优先级: 2')
    print(f'当前队列为空：{queue.is_empty()}')
    print(f'优先级最高的任务：{queue.get_first_task()}')
    queue.update_priority('a', 0)
    print('任务a的优先级设置为0')
    print(f'调整优先级后，优先级最高的任务：{queue.get_first_task()}')
    print(f'移除优先级最高的任务：{queue.dequeue()}')
    print(f'剩余任务中优先级最高的任务：{queue.get_first_task()}')
