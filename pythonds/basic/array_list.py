# -*- coding: utf-8 -*-

class ArrayList:
    """数组列表"""

    def __init__(self):
        self.array = []  # 模拟数组
        self.max_size = 0  # 数组容量
        self.last_index = 0  # 尾指针
        self.exponent = 0  # 扩容指数

    def __str__(self):
        return str(self.array[:self.last_index])

    def __len__(self):
        """len(self)"""
        return self.last_index

    def __getitem__(self, idx):
        """self[idx]"""
        if idx < 0 or idx >= self.last_index:
            raise IndexError('index out of range')
        return self.array[idx]

    def __setitem__(self, idx, item):
        """self[idx] = item"""
        if idx < 0 or idx >= self.last_index:
            raise IndexError('index out of range')
        self.array[idx] = item

    def __delitem__(self, idx):
        """del self[idx]"""
        self.pop(idx)

    def __iter__(self):
        """for i in self"""
        return iter(self.array[:self.last_index])

    def __resize(self):
        """数组扩容策略"""
        if self.exponent < 8:
            new_size = 2 ** self.exponent
            self.exponent += 1
        else:
            new_size = self.max_size + 2 ** self.exponent

        new_array = [0] * new_size
        for i in range(self.max_size):
            new_array[i] = self.array[i]

        self.array = new_array
        self.max_size = new_size

    def append(self, item):
        """
        追加操作

        Args:
            item: 添加的元素

        Returns:
            None
        """
        if self.last_index >= self.max_size:
            self.__resize()

        self.array[self.last_index] = item
        self.last_index += 1

    def insert(self, idx, item):
        """
        插入操作

        Args:
            idx: 插入元素的位置
            item: 插入的元素

        Returns:
            None
        """
        if self.last_index >= self.max_size:
            self.__resize()

        # 将列表尾到插入点的元素依次后移一位
        for i in range(self.last_index - 1, idx - 1, -1):
            self.array[i + 1] = self.array[i]

        self.array[min(self.last_index, idx)] = item
        self.last_index += 1

    def pop(self, idx=None):
        """
        删除操作

        Args:
            idx: 删除元素的位置

        Returns:
            被删除的元素
        """
        if idx is None:
            idx = self.last_index - 1
        if self.last_index == 0:
            raise IndexError('pop from empty list')
        if idx >= self.last_index:
            raise IndexError('pop index out of range')

        # 记录待删除元素
        item = arr[idx]
        # 将删除位置后面的所有元素依次前移一位
        for i in range(idx + 1, self.last_index):
            arr[i - 1] = arr[i]

        self.last_index -= 1
        return item

    def index(self, item):
        """
        查询指定元素的索引

        Args:
            item: 指定元素

        Returns:
            元素所在位置。若不在则返回-1
        """
        idx = -1

        for i in range(self.last_index):
            if self.array[i] == item:
                idx = i

        return idx


if __name__ == '__main__':
    arr = ArrayList()
    # arr.pop()
    print(arr)
    print(f'length: {len(arr)}')

    for i in range(3):
        arr.append(i)
    print(arr)
    print(f'length: {len(arr)}')
    print(arr, arr[0], arr[2])
    # print(arr[5])
    arr[0] = 10
    print(arr, arr[0])
    arr.insert(100, 12)
    arr.insert(0, 11)
    print(arr)

    for i in arr:
        print(i, end=' ')
    print()

    print(arr.pop())
    print(arr)
    print(f'length: {len(arr)}')
    print(arr.pop(0))
    print(arr)
    print(f'length: {len(arr)}')

    print(arr.index(10), arr.index(2), arr.index(11))

    del arr[0]
    print(arr)
    print(f'length: {len(arr)}')
