# -*- coding: utf-8 -*-

from typing import Union

from pythonds.trees.tree_node import TreeNode


class BinarySearchTree:
    """
    二叉搜索树

    删除节点时，从二叉树中移除节点
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
            self.__size -= 1  # 替换原节点的值，节点数未增加
            node.val = val

    def _get(self, key, node: TreeNode) -> Union[TreeNode, None]:
        if node is None:
            return None
        elif key < node.key:
            return self._get(key, node.left_child)
        elif key > node.key:
            return self._get(key, node.right_child)
        else:
            return node

    def _delete(self, node: TreeNode):
        if node.is_leaf():  # 待删除节点没有子节点
            # 根节点的情况已在delete()中处理
            if node.is_left_child():
                node.parent.left_child = None
            elif node.is_right_child():
                node.parent.right_child = None
        elif not node.has_both_child():  # 待删除节点只有一个子节点
            if node.left_child:  # 有左子节点
                if node.is_root():
                    self.__root = node.left_child
                else:
                    node.left_child.parent = node.parent
                    if node.is_left_child():
                        node.parent.left_child = node.left_child
                    else:
                        node.parent.right_child = node.left_child
            else:  # 有右子节点
                if node.is_root():
                    self.__root = node.right_child
                else:
                    node.right_child.parent = node.parent
                    if node.is_left_child():
                        node.parent.left_child = node.right_child
                    else:
                        node.parent.right_child = node.right_child
        else:  # 待删除节点有两个子节点
            successor_node = node.find_successor()
            # 将待删除节点替换成后继节点
            node.key = successor_node.key
            node.val = successor_node.val
            # 删除原本的后续节点
            self._delete(successor_node)

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
        elif self.__size == 1:
            self.__root = None
        else:
            self._delete(node)

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
