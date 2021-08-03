# -*- coding: utf-8 -*-

from pythonds.basic import Stack
from pythonds.trees import BinaryTree, preorder, inorder, postorder


# 前序遍历（迭代实现）
def preorder_iter(tree: BinaryTree):
    node = tree
    res, stack = [], Stack()

    while node or not stack.is_empty():
        if node:
            res.append(node.data)
            if node.right_child:
                stack.push(node.right_child)
            node = node.left_child
        else:
            node = stack.pop()

    return res


# 中序遍历（迭代实现）
def inorder_iter(tree: BinaryTree):
    node = tree
    res, stack = [], Stack()

    while node or not stack.is_empty():
        if node:
            stack.push(node)
            node = node.left_child
        else:
            node = stack.pop()
            res.append(node.data)
            node = node.right_child

    return res


# 后序遍历（迭代实现）
def postorder_iter(tree: BinaryTree):
    node = tree
    res, stack = [], Stack()
    prev_node = None  # 记录当前节点的上一个节点

    while node or not stack.is_empty():
        if node:
            stack.push(node)
            node = node.left_child
        else:
            node = stack.peek()
            if node.right_child and prev_node is not node.right_child:
                node = node.right_child
            else:
                stack.pop()
                res.append(node.data)
                prev_node = node
                node = None

    return res


def build_test_tree():
    root = BinaryTree('a')
    root.insert_left('b')
    root.insert_right('f')
    lnode = root.left_child
    lnode.insert_left('c')
    lnode.insert_right('d')
    lrnode = lnode.right_child
    lrnode.insert_right('e')
    rnode = root.right_child
    rnode.insert_left('g')

    return root


if __name__ == '__main__':
    tree = build_test_tree()
    print('前序:')
    preorder(tree)
    print(f'\n前序遍历: {preorder_iter(tree)}\n')
    print('中序:')
    inorder(tree)
    print(f'\n中序遍历: {inorder_iter(tree)}\n')
    print('后序:')
    postorder(tree)
    print(f'\n后序遍历: {postorder_iter(tree)}\n')
