# -*- coding: utf-8 -*-

from typing import Union


class HeaderNode:
    """跳表头节点"""

    def __init__(self):
        self.__down: Union[HeaderNode, DataNode, None] = None
        self.__next: Union[DataNode, None] = None

    @property
    def down(self):
        return self.__down

    @down.setter
    def down(self, node):
        self.__down = node

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, node):
        self.__next = node


class DataNode(HeaderNode):
    """数据节点"""

    def __init__(self, key, val):
        super().__init__()
        self.__key = key
        self.__val = val

    @property
    def key(self):
        return self.__key

    @property
    def value(self):
        return self.__val

    @value.setter
    def value(self, val):
        self.__val = val
