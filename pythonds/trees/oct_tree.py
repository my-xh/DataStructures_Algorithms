# -*- coding: utf-8 -*-

from typing import Optional


class OctTree:
    """八叉树"""

    class OctNode:
        """八叉树节点"""

        def __init__(self, parent=None, level=0, outer=None):
            self.r = 0  # 红色累计值
            self.g = 0  # 绿色累计值
            self.b = 0  # 蓝色累计值
            self.count = 0  # 相似颜色值的总数
            self.level = level  # 所在层级
            self.parent: OctTree.OctNode = parent  # 父节点
            self.outer: OctTree = outer  # 所属八叉树
            self.child: list[Optional[OctTree.OctNode]] = [None] * 8  # 子节点列表

        def _convert_to_key(self, r, g, b, level):
            """将颜色值转换成当前层级的子节点所对应的键"""
            shift = 8 - level - 1
            rc = (r >> (shift - 2) if shift >= 2 else r << (2 - shift)) & 0x4
            gc = (g >> (shift - 1) if shift >= 1 else g << (1 - shift)) & 0x2
            bc = b >> shift & 0x1

            return rc | gc | bc

        def insert(self, r, g, b, level, outer):
            """插入节点操作的具体逻辑"""
            if level >= outer._max_level:
                if self.count == 0:
                    outer._num_of_leaves += 1
                    outer._leaf_list.append(self)
                self.r += r
                self.g += g
                self.b += b
                self.count += 1
                return
            key = self._convert_to_key(r, g, b, level)
            if self.child[key] is None:
                self.child[key] = outer.OctNode(parent=self, level=level + 1, outer=outer)
            self.child[key].insert(r, g, b, level + 1, outer)

        def find(self, r, g, b, level):
            """查找节点操作的具体逻辑"""
            if self.count > 0 or level >= self.outer._max_level:
                # 返回目标节点的平均颜色值
                return (self.r // self.count,
                        self.g // self.count,
                        self.b // self.count)
            key = self._convert_to_key(r, g, b, level)
            if self.child[key] is None:
                print('error: No leaf node for this color!')
                return 0, 0, 0
            return self.child[key].find(r, g, b, level + 1)

        def merge(self):
            """合并当前节点的所有子节点，使当前节点成为新的叶子节点"""
            for node in self.child:
                if node is None:
                    continue
                if node.count > 0:
                    self.r += node.r
                    self.g += node.g
                    self.b += node.b
                    self.count += node.count
                    self.outer._num_of_leaves -= 1
                    self.outer._leaf_list.remove(node)
                else:
                    node.merge()

            for i in range(8):
                self.child[i] = None

    def __init__(self):
        self._root: Optional[OctTree.OctNode] = None  # 根节点
        self._max_level = 5  # 八叉树最大层级
        self._num_of_leaves = 0  # 叶子节点数量
        self._leaf_list: list[OctTree.OctNode] = []  # 叶子节点列表

    def _find_min_leaf(self):
        """查找出现次数最少的颜色所对应的叶子节点"""
        min_count = float('inf')
        max_level = 0
        min_leaf = None

        for leaf in self._leaf_list:
            if leaf.count <= min_count and leaf.level >= max_level:
                min_count = leaf.count
                max_level = leaf.level
                min_leaf = leaf

        return min_leaf

    def insert(self, r, g, b):
        """
        往八叉树中插入一个节点，以红、绿、蓝的值为键

        Args:
            r: 红色值
            g: 绿色值
            b: 蓝色值

        Returns:
            None
        """
        if self._root is None:
            self._root = self.OctNode(outer=self)
        else:
            self._root.insert(r, g, b, 0, self)

    def find(self, r, g, b):
        """
        以红、绿、蓝的值为搜索键，查找一个节点或者与其最相似的节点的颜色值

        Args:
            r: 红色值
            g: 绿色值
            b: 蓝色值

        Returns:
            (nr, ng, nb) - 与指定颜色最相似的节点的颜色值
        """
        if self._root:
            return self._root.find(r, g, b, 0)
        else:
            return 0, 0, 0

    def reduce(self, n):
        """
        缩小八叉树，减少叶子节点的数量

        Args:
            n: 八叉树叶子节点数的最大值

        Returns:
            None
        """
        if n < 1:
            return
        while self._num_of_leaves > n:
            min_leaf = self._find_min_leaf()
            min_leaf.parent.merge()
            self._leaf_list.append(min_leaf.parent)
            self._num_of_leaves += 1
