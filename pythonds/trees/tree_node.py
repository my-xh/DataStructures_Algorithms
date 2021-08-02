# -*- coding: utf-8 -*-

class TreeNode:
    """树节点"""

    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key  # 键
        self.val = val  # 值
        self.left_child: TreeNode = left  # 左子节点
        self.right_child: TreeNode = right  # 右子节点
        self.parent: TreeNode = parent  # 父节点
        self.__status = True  # 标记节点是否被删除

    def __iter__(self):
        if self.left_child:
            yield from self.left_child
        if self.is_enable():
            yield self.key
        if self.right_child:
            yield from self.right_child

    def is_enable(self):
        return self.__status

    def enable(self):
        self.__status = True

    def disable(self):
        self.__status = False

    def is_left_child(self):
        return self.parent and (self.parent.left_child is self)

    def is_right_child(self):
        return self.parent and (self.parent.right_child is self)

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not self.is_root() and not self.left_child and not self.right_child

    def has_any_child(self):
        return self.left_child or self.right_child

    def has_both_child(self):
        return self.left_child and self.right_child

    def find_successor(self) -> "TreeNode":
        """寻找后继节点"""
        node = None
        if self.right_child:  # 有右子节点, 后继节点是右子树的最小节点
            node = self.right_child
            while node.left_child:
                node = node.left_child
        elif self.is_left_child():  # 没有右子节点，是父节点的左子节点，后继节点是父节点
            node = self.parent
        elif self.is_right_child():  # 没有右子节点，是父节点的右子节点，后继节点是父节点的后继节点
            self.parent.right_child = None  # 暂时清空父节点的右子树
            node = self.parent.find_successor()
            self.parent.right_child = self  # 恢复父节点的右子树

        return node
