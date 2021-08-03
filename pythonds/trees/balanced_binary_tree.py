# -*- coding: utf-8 -*-

from pythonds.trees._binary_search_tree import BinarySearchTree
from pythonds.trees.tree_node import TreeNode


class AVLTree(BinarySearchTree):
    """平衡二叉搜索树"""

    def _rotate_left(self, node: TreeNode):
        """
        左旋以指定节点为根的子树

        Args:
            node: 当前节点

        Returns:
            左旋后子树的新根节点
        """
        # 右子节点成为新的根节点
        root = node.right_child
        root.parent = node.parent
        if node.is_left_child():
            node.parent.left_child = root
        elif node.is_right_child():
            node.parent.right_child = root
        else:
            # 原根节点是整棵树的根节点，则改变根节点
            self._set_root(root)

        # 新根节点的左子节点成为原根节点的右子节点
        node.right_child = root.left_child
        if root.left_child:
            root.left_child.parent = node

        # 原根节点成为新根节点的左子节点
        root.left_child = node
        node.parent = root

        # 设原根节点为a, 新根节点为b, 左旋后的平衡因子为：
        # Fa′ = Fa + 1 - min(Fb, 0)
        # Fb′ = Fb + 1 + max(Fa′, 0)
        node.balance_factor += 1 - min(root.balance_factor, 0)
        root.balance_factor += 1 + max(node.balance_factor, 0)

        return root

    def _rotate_right(self, node: TreeNode):
        """
        右旋以指定节点为根的子树

        Args:
            node: 当前节点

        Returns:
            右旋后子树的新根节点
        """
        # 左子节点成为新的根节点
        root = node.left_child
        root.parent = node.parent
        if node.is_left_child():
            node.parent.left_child = root
        elif node.is_right_child():
            node.parent.right_child = root
        else:
            # 原根节点是整棵树的根节点，则改变根节点
            self._set_root(root)

        # 新根节点的右子节点成为原根节点的左子节点
        node.left_child = root.right_child
        if root.right_child:
            root.right_child.parent = node

        # 原根节点成为新根节点的右子节点
        root.right_child = node
        node.parent = root

        # 设原根节点为a, 新根节点为b, 右旋后的平衡因子为：
        # Fa′ = Fa - 1 - max(Fb, 0)
        # Fb′ = Fb - 1 + min(Fa′, 0)
        node.balance_factor -= 1 + max(root.balance_factor, 0)
        root.balance_factor -= 1 - min(node.balance_factor, 0)

        return root

    def _rebalance(self, node: TreeNode):
        """
        重新平衡以指定节点为根的子树

        Args:
            node: 当前节点

        Returns:
            平衡后子树的新根节点
        """
        if node.balance_factor < 0:
            # 当前节点需要左旋
            # 先检查其右子节点是否需要右旋
            if node.right_child.balance_factor > 0:
                self._rotate_right(node.right_child)
            node = self._rotate_left(node)
        elif node.balance_factor > 0:
            # 当前节点需要右旋
            # 先检查其左子节点是否需要左旋
            if node.left_child.balance_factor < 0:
                self._rotate_left(node.left_child)
            node = self._rotate_right(node)

        return node

    def _update_balance(self, node: TreeNode, incre):
        """
        更新指定节点的父节点的平衡因子

        Args:
            node: 当前节点
            incre: 平衡因子增量，新增为1，删除为-1

        Returns:
            None
        """
        # 当前节点的平衡因子过小或过大时，对该节点执行重新平衡操作
        if node.balance_factor < -1 or node.balance_factor > 1:
            node = self._rebalance(node)
            # 新增节点时，重新平衡后不用更新后续祖先节点的平衡因子
            # 删除节点时，重新平衡后要从新的子树根节点开始继续更新后续祖先节点的平衡因子
            if incre > 0:
                return

        if node.is_root():
            return
        if node.is_left_child():
            node.parent.balance_factor += incre
        elif node.is_right_child():
            node.parent.balance_factor -= incre

        # 新增节点时，若父节点的平衡因子更新后为0，说明以父节点为根的子树高度未发生变化，后续祖先节点不用更新平衡因子;
        # 若父节点的平衡因子更新后不为0，则需要继续更新后续祖先节点的平衡因子
        if incre > 0 and node.parent.balance_factor != 0:
            self._update_balance(node.parent, incre)
        # 删除节点时，若父节点的平衡因子更新后为-1或者1，说明以父节点为根的子树高度未发生变化，后续祖先节点不用更新平衡因子；
        # 若父节点的平衡因子更新后不为-1或者1，则需要继续更新后续祖先节点的平衡因子
        elif incre < 0 and node.parent.balance_factor not in {-1, 1}:
            self._update_balance(node.parent, incre)

    # 重写_put()方法
    def _put(self, key, val, node: TreeNode):
        new_node = None
        if key < node.key:
            if node.left_child:
                self._put(key, val, node.left_child)
            else:
                new_node = TreeNode(key, val, parent=node)
                node.left_child = new_node
                self._size += 1
        elif key > node.key:
            if node.right_child:
                self._put(key, val, node.right_child)
            else:
                new_node = TreeNode(key, val, parent=node)
                node.right_child = new_node
                self._size += 1
        else:
            # 替换原节点的值，节点数未增加
            node.val = val

        # 新增节点时，更新平衡因子
        if new_node:
            self._update_balance(new_node, incre=1)

    # 重写_delete()方法
    def _delete(self, node: TreeNode):
        # 当待删除节点有两个子节点时，不用更新平衡因子
        if not node.has_both_child():
            self._update_balance(node, incre=-1)

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


if __name__ == '__main__':
    avl = AVLTree()
    avl[5] = 0
    avl[3] = 0
    print(f'（新增测试）当前AVL的节点个数: {len(avl)}, 根节点: {avl._get_root().key}')
    avl[2] = 0
    print(f'（新增测试）当前AVL的节点个数: {len(avl)}, 根节点: {avl._get_root().key}')
    avl[2] = 1
    print(f'（替换测试）当前AVL的节点个数: {len(avl)}, 根节点: {avl._get_root().key}')

    avl[4] = 0
    avl[7] = 0
    avl[6] = 0
    avl[8] = 0
    avl[9] = 0
    avl[1] = 0
    print(f'（新增测试）当前AVL的节点个数: {len(avl)}, 根节点: {avl._get_root().key}')
    print(f'遍历AVL: {", ".join(str(i) for i in avl)}')

    del avl[5]
    print(f'（删除测试）当前AVL的节点个数: {len(avl)}, 根节点: {avl._get_root().key}')
    print(f'遍历AVL: {", ".join(str(i) for i in avl)}')
