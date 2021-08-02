# -*- coding: utf-8 -*-

FIRST = 1


class BinaryHeap:
    """(最小)二叉堆"""

    def __init__(self):
        self._heap = [0]  # 堆的内部表示
        self.__size = 0  # 堆的大小

    def __str__(self):
        return str(self._heap[FIRST:])

    @staticmethod
    def _parent(idx):
        return parent if (parent := idx // 2) > 0 else None

    def _left_child(self, idx):
        return left if (left := idx * 2) <= self.__size else None

    def _right_child(self, idx):
        return right if (right := idx * 2 + 1) <= self.__size else None

    def _min_child(self, idx):
        left, right = self._left_child(idx), self._right_child(idx)
        if right is None:
            return left
        elif self._heap[left] < self._heap[right]:
            return left
        else:
            return right

    def _swap(self, idx1, idx2):
        self._heap[idx1], self._heap[idx2] = self._heap[idx2], self._heap[idx1]

    def _shift_up(self, idx=None):
        if idx is None:
            idx = self.__size
        while (parent := self._parent(idx)) is not None:
            if self._heap[parent] <= self._heap[idx]:
                break
            self._swap(idx, parent)
            idx = parent

    def _shift_down(self, idx=FIRST):
        while (min_child := self._min_child(idx)) is not None:
            if self._heap[idx] <= self._heap[min_child]:
                break
            self._swap(idx, min_child)
            idx = min_child

    @property
    def size(self):
        return self.__size

    def is_empty(self):
        return self.__size == 0

    def find_min(self):
        if self.__size > 0:
            return self._heap[FIRST]

    def push(self, key):
        self._heap.append(key)
        self.__size += 1
        # 上浮检查调整堆结构
        self._shift_up()

    def pop(self):
        if self.__size == 0:
            raise IndexError('index out of range')

        val = self.find_min()
        self._heap[FIRST] = self._heap[self.__size]
        self._heap.pop()
        self.__size -= 1
        # 下沉检查调整堆结构
        self._shift_down()

        return val

    def index(self, key):
        idx, found = FIRST, False

        while idx <= self.__size and not found:
            if self._heap[idx] == key:
                found = True
            else:
                idx += 1

        if not found:
            return -1
        else:
            return idx

    def replace(self, idx, key):
        old, self._heap[idx] = self._heap[idx], key
        if key > old:
            self._shift_down(idx)
        elif key < old:
            self._shift_up(idx)

    def build_heap(self, arr: list):
        self._heap = [0]
        self._heap.extend(arr)
        self.__size = len(arr)
        # 从最后一个非叶子节点到根节点，依次对每个节点进行下沉检查调整堆结构
        idx = self.__size // 2
        while idx > 0:
            self._shift_down(idx)
            idx -= 1

        return self


if __name__ == '__main__':
    heap = BinaryHeap()
    arr = [5, 9, 11, 14, 18, 19, 21, 33, 17, 27]
    heap.build_heap(arr)
    print(f'初始堆: {heap}')
    heap.push(7)
    print(f'向堆中添加7后: {heap}')
    print('*' * 50)

    heap.build_heap(arr)
    print(f'初始堆: {heap}')
    print(f'从堆中移除最小值: {heap.pop()}')
    print(f'移除最小值后的堆: {heap}')
    print('*' * 50)

    arr = [9, 6, 5, 2, 3]
    heap.build_heap(arr)
    print(f'通过 {arr} 初始化的堆: {heap}')
