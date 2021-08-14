# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class Node:
    """节点"""

    def __init__(self, item):
        self.__data = item
        self.__next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, item):
        self.__data = item

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, node):
        self.__next = node


class List(metaclass=ABCMeta):
    """列表"""

    def __init__(self):
        self.head = None

    @classmethod
    @property
    def __class_name(cls):
        return cls.__name__

    def __str__(self):
        cur, nodes = self.head, [self.__class_name + '[head']

        while cur is not None:
            nodes.append(str(cur.data))
            cur = cur.next
        nodes.append('null]')

        return ' -> '.join(nodes)

    def is_empty(self):
        return self.head is None

    def length(self):
        cur, cnt = self.head, 0

        while cur is not None:
            cnt += 1
            cur = cur.next

        return cnt

    @abstractmethod
    def add(self, item):
        ...

    @abstractmethod
    def search(self, item):
        ...

    @abstractmethod
    def remove(self, item):
        ...

    @abstractmethod
    def index(self, item):
        ...

    def pop(self, pos=None):
        pre, cur, cnt = None, self.head, 0

        if cur is None:
            return None  # 没有节点删除，直接返回

        while (pos is None or cnt < pos) and cur.next is not None:
            pre = cur
            cur = cur.next
            cnt += 1

        if pre is None:
            self.head = cur.next
        else:
            pre.next = cur.next
        return cur.data


class UnorderedList(List):
    """无序列表"""

    def add(self, item):
        node = Node(item)
        node.next = self.head
        self.head = node

    def search(self, item):
        cur, found = self.head, False

        while cur is not None and not found:
            if cur.data == item:
                found = True
            else:
                cur = cur.next

        return found

    def remove(self, item):
        pre, cur, found = None, self.head, False

        while cur is not None and not found:
            if cur.data == item:
                found = True
            else:
                pre = cur
                cur = cur.next

        if not found:
            return
        elif pre is None:
            self.head = cur.next
        else:
            pre.next = cur.next

    def append(self, item):
        cur, node = self.head, Node(item)

        while cur.next is not None:
            cur = cur.next

        cur.next = node

    def insert(self, pos, item):
        if pos == 0:
            return self.add(item)

        cur, cnt, node = self.head, 1, Node(item)

        while cnt < pos and cur.next is not None:
            cnt += 1
            cur = cur.next

        node.next = cur.next
        cur.next = node

    def index(self, item):
        cur, idx, found = self.head, 0, False

        while cur is not None and not found:
            if cur.data == item:
                found = True
            else:
                cur = cur.next
                idx += 1

        if not found:
            return -1
        else:
            return idx


class OrderedList(List):
    """有序列表"""

    def add(self, item):
        pre, cur, node = None, self.head, Node(item)

        while cur is not None and cur.data <= item:
            pre = cur
            cur = cur.next

        if pre is None:
            node.next = self.head
            self.head = node
        else:
            node.next = pre.next
            pre.next = node

    def search(self, item):
        cur, found = self.head, False

        while cur is not None and not found and cur.data <= item:
            if cur.data == item:
                found = True
            else:
                cur = cur.next

        return found

    def remove(self, item):
        pre, cur, found = None, self.head, False

        while cur is not None and not found and cur.data <= item:
            if cur.data == item:
                found = True
            else:
                pre = cur
                cur = cur.next

        if not found:
            return
        elif pre is None:
            self.head = cur.next
        else:
            pre.next = cur.next

    def index(self, item):
        cur, idx, found = self.head, 0, False

        while cur is not None and not found and cur.data <= item:
            if cur.data == item:
                found = True
            else:
                idx += 1
                cur = cur.next

        if not found:
            return -1
        else:
            return idx


if __name__ == '__main__':
    mylist = UnorderedList()
    print(mylist.is_empty())
    mylist.add(31)
    print(mylist.is_empty())
    mylist.add(77)
    mylist.add(17)
    mylist.add(93)
    mylist.add(26)
    mylist.add(54)
    print(mylist)
    print(mylist.length())
    print(mylist.search(17), mylist.search(54), mylist.search(78))
    mylist.remove(54)
    print(mylist)
    mylist.append(43)
    print(mylist)
    mylist.insert(1, 11)
    print(mylist)
    mylist.insert(10, 22)
    print(mylist)
    print(mylist.index(26), mylist.index(22), mylist.index(3))
    print(mylist.pop(0))
    print(mylist)
    print(mylist.pop(6))
    print(mylist)
    print(mylist.pop(10))
    print(mylist)
    print(mylist.pop())
    print(mylist)

    print('*' * 50)

    olist = OrderedList()
    print(olist.is_empty())
    olist.add(31)
    print(olist.is_empty())
    olist.add(77)
    olist.add(17)
    olist.add(93)
    olist.add(26)
    olist.add(54)
    print(olist)
    print(olist.length())
    print(olist.search(17), olist.search(54), olist.search(78))
    olist.remove(54)
    print(olist)
    print(olist.index(17), olist.index(93), olist.index(27))
    print(olist.pop(0))
    print(olist)
    print(olist.pop(3))
    print(olist)
    print(olist.pop(10))
    print(olist)
    print(olist.pop())
    print(olist)
