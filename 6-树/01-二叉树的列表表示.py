# -*- coding: utf-8 -*-

# 创建二叉树
def BinaryTree(root):
    return [root, [], []]


# 插入左子树
def insert_left(root, child):
    tmp = root.pop(1)
    if len(tmp) > 0:
        root.insert(1, [child, tmp, []])
    else:
        root.insert(1, [child, [], []])

    return root


# 插入右子树
def insert_right(root, child):
    tmp = root.pop(2)
    if len(tmp) > 0:
        root.insert(2, [child, [], tmp])
    else:
        root.insert(2, [child, [], []])

    return root


# 设置当前节点的值
def set_val(root, val):
    root[0] = val


# 获取当前节点的值
def get_val(root):
    return root[0]


# 获取左子树
def get_left(root):
    return root[1]


# 获取右子树
def get_right(root):
    return root[2]


if __name__ == '__main__':
    r = BinaryTree(3)
    print(insert_left(r, 4))
    print(insert_left(r, 5))
    print(insert_right(r, 6))
    print(insert_right(r, 7))
    l = get_left(r)
    print(l)
    set_val(l, 9)
    print(r)
    print(insert_left(l, 11))
    print(r)
    print(get_right(get_right(r)))
