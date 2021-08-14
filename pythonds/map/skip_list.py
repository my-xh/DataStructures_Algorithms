# -*- coding: utf-8 -*-

from random import randrange
from typing import Union

from pythonds.basic import Stack
from pythonds.map.node import HeaderNode, DataNode


class Coin:
    """硬币"""

    def __init__(self):
        self.__is_first = True

    # 模拟投硬币，第一次抛硬币必为正面
    def flip(self):
        if self.__is_first:
            self.__is_first = False
            return True
        return randrange(2) == 1


class SkipList:
    """跳表"""

    def __init__(self):
        self._head = HeaderNode()  # 跳表最顶层的头节点

    def _get_bottom_head(self):
        """获取跳表最底层的头节点"""
        node = self._head
        while node.down is not None:
            node = node.down

        return node

    def _search(self, key, on_delete=False):
        """
        跳表 search/insert/delete 方法通用查询逻辑

        Args:
            key: 查询的键
            on_delete: delete方法特有逻辑

        Returns:
            目标节点, 目标节点的前驱节点列表
        """
        node: Union[HeaderNode, DataNode] = self._head
        tower_stack = Stack()  # 前驱节点列表（通过栈维护由底向上的顺序）
        found = False

        while node is not None and not found:
            if node.next is None or node.next.key > key:
                tower_stack.push(node)  # 降到下一层前保存当前层的前驱节点
                node = node.down
            elif node.next.key <= key:
                node = node.next
                if node.key == key:
                    found = True

        if found and on_delete:
            # 删除操作中，需要继续往下找到每一层目标节点的前驱节点
            pre_node = self._head if tower_stack.is_empty() else tower_stack.pop()
            while pre_node is not None:
                if pre_node.next is None or pre_node.next.key >= key:
                    tower_stack.push(pre_node)
                    pre_node = pre_node.down
                else:
                    pre_node = pre_node.next

        return node, tower_stack

    @staticmethod
    def _update(top_node: DataNode, val):
        """
        更新指定节点的值

        Args:
            top_node: 待更新节点
            val: 待更新的值

        Returns:
            None
        """
        # 只更新顶层节点的值（仅适用于替换操作，不满足values方法）
        # top_node.value = val
        # 从顶层向下更新所有相同键的节点的值
        while top_node:
            top_node.value = val
            top_node = top_node.down

    def search(self, key):
        """
        在跳表中查询指定键的节点

        Args:
            key: 查询的键

        Returns:
            目标节点
        """
        node, _ = self._search(key)

        return node

    def insert(self, key, val):
        """
        在跳表中插入新节点

        Args:
            key: 待插入节点的键
            val: 待插入节点的值

        Returns:
            None
        """
        node, tower_stack = self._search(key)

        # 键为key的节点已存在，仅更新节点值
        if node is not None:
            self._update(node, val)
            return

        coin = Coin()  # 硬币
        pre_node: Union[HeaderNode, DataNode]  # 前驱节点
        top_node: Union[DataNode, None] = None  # 顶层目标节点

        # 通过抛硬币决定目标节点的层数
        while coin.flip():
            node = DataNode(key, val)
            if not tower_stack.is_empty():
                # 前驱节点列表不为空
                pre_node = tower_stack.pop()
                node.next, pre_node.next = pre_node.next, node  # 将当前层目标节点插入跳表
            else:
                # 前驱节点列表为空，增加新层头节点作为前驱节点
                new_head = HeaderNode()
                new_head.down, self._head = self._head, new_head  # 增加新层头节点
                new_head.next = node  # 插入新层目标节点
            # 当前目标节点成为新的顶层目标节点
            node.down, top_node = top_node, node

    def delete(self, key):
        """
        在跳表中删除指定节点

        Args:
            key: 待删除节点的键

        Returns:
            None
        """
        node, tower_stack = self._search(key, on_delete=True)

        # 键为key的节点不存在，不用删除节点
        if node is None:
            return

        # 从跳表最底层向上，依次移除每一层的目标节点
        stop = False
        pre_node: Union[HeaderNode, DataNode]
        while not tower_stack.is_empty() and not stop:
            pre_node = tower_stack.pop()
            if pre_node.next is node:
                # 已到达顶层目标节点
                stop = True
            pre_node.next = pre_node.next.next

        # 跳表最顶层没有数据节点时，跳表层数-1（跳表至少有一层）
        while self._head.next is None and self._head.down is not None:
            self._head = self._head.down

    def keys(self):
        """
        查找跳表中所有的键

        Returns:
            节点键列表
        """
        # 获取到最底层的头指针
        node = self._get_bottom_head()
        # 向右依次遍历每个数据节点的键
        key_list = []
        while node.next is not None:
            node = node.next
            key_list.append(node.key)

        return key_list

    def values(self):
        """
        查找跳表中所有的值

        Returns:
            节点值列表
        """
        # 获取到最底层的头指针
        node = self._get_bottom_head()
        # 向右依次遍历每个数据节点的值
        value_list = []
        while node.next is not None:
            node = node.next
            value_list.append(node.value)

        return value_list

    def items(self):
        """
        查找跳表中所有的键值对

        Returns:
            节点键值对列表
        """
        # 获取到最底层的头指针
        node = self._get_bottom_head()
        # 向右依次遍历每个数据节点的键值对
        item_list = []
        while node.next is not None:
            node = node.next
            item_list.append((node.key, node.value))

        return item_list
