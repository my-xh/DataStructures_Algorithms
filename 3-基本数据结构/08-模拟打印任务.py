# -*- coding: utf-8 -*-

import random

from pythonds.basic import Queue


class Task:
    """任务"""

    def __init__(self, timestamp):
        self.__timestamp = timestamp
        self.__pages = random.randrange(1, 21)

    @property
    def timestamp(self):
        return self.__timestamp

    @property
    def pages(self):
        return self.__pages

    def wait_time(self, current_time):
        return current_time - self.timestamp


class Printer:
    """打印机"""

    def __init__(self, ppm):
        self.__page_rate = ppm
        self.__current_task = None
        self.__time_remaining = 0

    def tick(self):
        if self.__current_task is not None:
            self.__time_remaining -= 1
            if self.__time_remaining <= 0:
                self.__current_task = None

    def busy(self):
        return self.__current_task is not None

    def start_next(self, task: Task):
        self.__current_task = task
        self.__time_remaining = task.pages // self.__page_rate * 60


def new_print_task():
    return random.randrange(1, 181) == 180


def simulation(total_seconds, pages_per_minute):
    queue, wait_times = Queue(), []
    printer = Printer(pages_per_minute)

    for second in range(total_seconds):
        if new_print_task():
            queue.enqueue(Task(second))
        if not printer.busy() and not queue.is_empty():
            task = queue.dequeue()
            wait_times.append(task.wait_time(second))
            printer.start_next(task)
        printer.tick()

    print(f'Average Wait {sum(wait_times) / len(wait_times):6.2f} secs {queue.size():2d} tasks remaining.')


if __name__ == '__main__':
    for i in range(10):
        simulation(3600, 5)
    print('*' * 50)
    for i in range(10):
        simulation(3600, 10)
