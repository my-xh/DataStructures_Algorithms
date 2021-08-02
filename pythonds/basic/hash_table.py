# -*- coding: utf-8 -*-

class HashTable:
    """哈希表"""

    def __init__(self):
        self._size = 11
        self._slots = [None] * self._size
        self._data = [None] * self._size

    def __len__(self):
        length = 0
        for key in self._slots:
            if key is not None:
                length += 1

        return length

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, val):
        self.put(key, val)

    def __delitem__(self, key):
        start_slot = hash_value = self._hash(key)
        found, stop = False, False

        while self._slots[hash_value] is not None and not found and not stop:
            if self._slots[hash_value] == key:
                self._slots[hash_value] = None
                found = True
            else:
                hash_value = self._rehash(hash_value)
                if hash_value == start_slot:
                    stop = True

    def __contains__(self, key):
        # todo: 考虑value为None的情况
        return self.get(key) is not None

    def _hash(self, key):
        return key % self._size

    def _rehash(self, old_hash):
        return (old_hash + 1) % self._size

    def put(self, key, val):
        hash_value = self._hash(key)
        while self._slots[hash_value] is not None and self._slots[hash_value] != key:
            hash_value = self._rehash(hash_value)
        if self._slots[hash_value] is None:
            # 新增
            self._slots[hash_value] = key
            self._data[hash_value] = val
        else:
            # 替换
            self._data[hash_value] = val

    def get(self, key):
        start_slot = hash_value = self._hash(key)
        data, found, stop = None, False, False

        while self._slots[hash_value] is not None and not found and not stop:
            if self._slots[hash_value] == key:
                data = self._data[hash_value]
                found = True
            else:
                hash_value = self._rehash(hash_value)
                if hash_value == start_slot:
                    stop = True

        return data


if __name__ == '__main__':
    mp = HashTable()
    mp[54] = 'cat'
    mp[26] = 'dog'
    mp[93] = 'lion'
    mp[17] = 'tiger'
    mp[77] = 'bird'
    mp[31] = 'cow'
    mp[44] = 'goat'
    mp[55] = 'pig'
    mp[20] = 'chicken'
    print(mp[20], mp[17])
    mp[20] = 'duck'
    print(mp[20])
    print(mp[99])
    print(len(mp))
    mp[35] = 'chicken'
    print(mp[35])
    print(len(mp))
    print(f'35 in mp: {35 in mp}')
    del mp[35]
    print(mp[35])
    print(len(mp))
    print(f'35 in mp: {35 in mp}')
