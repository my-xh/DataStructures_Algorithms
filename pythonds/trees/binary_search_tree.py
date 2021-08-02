# -*- coding: utf-8 -*-

from typing import Union

from pythonds.trees.tree_node import TreeNode


class BinarySearchTree:
    """
    二叉搜索树

    删除节点时，不从树中移除，仅禁用该节点
    """

    def __init__(self):
        self.__root = None
        self.__size = 0

    def __len__(self):
        return self.__size

    def __contains__(self, key):
        return True if self._get(key, self.__root) else False

    def __setitem__(self, key, val):
        self.put(key, val)

    def __getitem__(self, key):
        node = self._get(key, self.__root)
        if node is None:
            raise KeyError(key)
        else:
            return node.val

    def __delitem__(self, key):
        self.delete(key)

    def __iter__(self):
        return self.__root.__iter__()

    def _put(self, key, val, node: TreeNode):
        if key < node.key:
            if node.left_child:
                self._put(key, val, node.left_child)
            else:
                node.left_child = TreeNode(key, val, parent=node)
        elif key > node.key:
            if node.right_child:
                self._put(key, val, node.right_child)
            else:
                node.right_child = TreeNode(key, val, parent=node)
        else:
            if node.is_enable():
                self.__size -= 1  # 节点值被替换前未禁用，节点数量不增加
            else:
                node.enable()  # 节点值被替换前已被禁用，启用节点且节点数+1
            node.val = val

    def _get(self, key, node: TreeNode) -> Union[TreeNode, None]:
        if node is None:
            return None
        elif key < node.key:
            return self._get(key, node.left_child)
        elif key > node.key:
            return self._get(key, node.right_child)
        elif not node.is_enable():
            return None
        else:
            return node

    def put(self, key, val):
        if self.__root is None:
            self.__root = TreeNode(key, val)
        else:
            self._put(key, val, self.__root)

        self.__size += 1

    def get(self, key, default=None):
        if self.__root is None:
            return default
        elif (node := self._get(key, self.__root)) is not None:
            return node.val

        return default

    def delete(self, key):
        node = self._get(key, self.__root)
        if node is None:
            raise KeyError(key)
        else:
            node.disable()
            self.__size -= 1


if __name__ == '__main__':
    mp = BinarySearchTree()
    mp[54] = 'cat'
    mp[26] = 'dog'
    mp[93] = 'lion'
    mp[26] = 'dog+'
    print(mp[26])
    print(mp.get(14, 'not found'))
    print(14 in mp)
    print(26 in mp)
    print(len(mp))
    for key in mp:
        print(key, mp[key])
    print('*' * 50)

    # del mp[12]
    del mp[26]
    # print(mp[26])
    print(26 in mp)
    print(len(mp))
    for key in mp:
        print(key, mp[key])
    print('*' * 50)

    mp[26] = 'dog'
    print(mp[26])
    print(26 in mp)
    print(len(mp))
    for key in mp:
        print(key, mp[key])
