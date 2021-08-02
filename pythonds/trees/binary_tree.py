# -*- coding: utf-8 -*-

from typing import Union


class BinaryTree:
    """二叉树"""

    def __init__(self, item=None):
        self.__data = item
        self.__left = None
        self.__right = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, item):
        self.__data = item

    @property
    def left_child(self) -> Union["BinaryTree", None]:
        return self.__left

    @left_child.setter
    def left_child(self, node: Union["BinaryTree", None]):
        self.__left = node

    @property
    def right_child(self) -> Union["BinaryTree", None]:
        return self.__right

    @right_child.setter
    def right_child(self, node: Union["BinaryTree", None]):
        self.__right = node

    def insert_left(self, item=None):
        node = BinaryTree(item)
        if self.left_child is not None:
            node.left_child = self.left_child
        self.left_child = node

    def insert_right(self, item=None):
        node = BinaryTree(item)
        if self.right_child is not None:
            node.right_child = self.right_child
        self.right_child = node


# 外部前序遍历（递归实现）
def preorder(tree: BinaryTree):
    if tree is None:
        return
    print(tree.data, end=' ')
    preorder(tree.left_child)
    preorder(tree.right_child)


# 外部中序遍历（递归实现）
def inorder(tree: BinaryTree):
    if tree is None:
        return
    inorder(tree.left_child)
    print(tree.data, end=' ')
    inorder(tree.right_child)


# 外部后序遍历（递归实现）
def postorder(tree: BinaryTree):
    if tree is None:
        return
    postorder(tree.left_child)
    postorder(tree.right_child)
    print(tree.data, end=' ')


if __name__ == '__main__':
    tree = BinaryTree('a')
    print(tree.data)
    print(tree.left_child)
    tree.insert_left('b')
    print(tree.left_child)
    print(tree.left_child.data)
    tree.insert_right('c')
    print(tree.right_child)
    print(tree.right_child.data)
    tree.right_child.data = 'hello'
    print(tree.right_child.data)
