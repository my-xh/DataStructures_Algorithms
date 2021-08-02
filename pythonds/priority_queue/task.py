# -*- coding: utf-8 -*-


from functools import total_ordering


@total_ordering
class Task:
    """任务"""

    def __init__(self, key, priority):
        self.__key = key
        self.priority = priority

    def __lt__(self, other: "Task"):
        return self.priority < other.priority

    def __eq__(self, other: "Task"):
        return self.priority == other.priority

    @property
    def key(self):
        return self.__key


if __name__ == '__main__':
    task1 = Task('task1', 1)
    task2 = Task('task2', 2)
    print(task1.key, task1.priority)
    print(task1 <= task2)
