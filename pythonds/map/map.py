# -*- coding: utf-8 -*-

from pythonds.map.node import DataNode
from pythonds.map.skip_list import SkipList


class Map:
    """映射"""

    def __init__(self):
        self.__container = SkipList()

    def __getitem__(self, key):
        """self[key]"""
        node: DataNode = self.__container.search(key)
        if node is None:
            raise KeyError(key)
        else:
            return node.value

    def __setitem__(self, key, val):
        """self[key] = val"""
        self.put(key, val)

    def __delitem__(self, key):
        """del self[key]"""
        self.__container.delete(key)

    def get(self, key, default=None):
        """
        查询操作调用接口

        Args:
            key: 查询的键
            default: 查询失败时返回的结果

        Returns:
            查询到的值
        """
        node: DataNode = self.__container.search(key)
        return node.value if node is not None else default

    def put(self, key, val):
        """
        新增操作调用接口，键已存在时替换值

        Args:
            key: 新增的键
            val: 新增的值

        Returns:
            None
        """
        self.__container.insert(key, val)

    def keys(self):
        """
        返回映射中键的列表

        Returns:
            键的列表
        """
        yield from self.__container.keys()

    def values(self):
        """
        返回映射中值的列表

        Returns:
            值的列表
        """
        yield from self.__container.values()

    def items(self):
        """
        返回映射中键值对的列表

        Returns:
            键值对列表
        """
        yield from self.__container.items()


if __name__ == '__main__':
    mp = Map()
    mp[5] = 'lion'
    mp[10] = 'bird'
    mp[1] = 'cat'
    print(mp[1])

    mp[3] = 'dog'
    mp[3] = 'tiger'
    print(mp[3])

    print(mp.get(2))
    # print(mp[2])

    del mp[3]
    print(mp.get(3))

    print(list(mp.keys()))
    print(list(mp.values()))
    for k, v in mp.items():
        print(f'{k} -> {v}')
