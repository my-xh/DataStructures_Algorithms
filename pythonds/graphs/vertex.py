# -*- coding: utf-8 -*-
from functools import total_ordering


@total_ordering
class Vertex:
    """顶点"""
    __connect: dict["Vertex", int]

    def __init__(self, key):
        self.__id = key
        self.__connect = {}
        self.color = 'white'
        self.predecessor = None
        self.distance = 0
        self.discovery_time = 0  # 首次访问时间
        self.finish_time = 0  # 结束访问时间

    def __str__(self):
        return f'<Vertex id:{self.__id} time:({self.discovery_time}/{self.finish_time}) ' \
               f'color:{self.color} predecessor:{self.predecessor.id if self.predecessor else None} ' \
               f'connect_to:{[v.id for v in self.__connect]}>'

    def __lt__(self, other: "Vertex"):
        return self.id < other.id

    def __eq__(self, other: "Vertex"):
        return self.id == other.id

    def __hash__(self):
        return super().__hash__()

    @property
    def id(self):
        return self.__id

    @property
    def connect(self):
        yield from self.__connect.keys()

    def add_neighbor(self, vertex: "Vertex", weight=0):
        self.__connect[vertex] = weight

    def get_weight(self, vertex: "Vertex", default=0):
        return self.__connect.get(vertex, default)


if __name__ == '__main__':
    v1 = Vertex(0)
    v2 = Vertex(1)
    v1.add_neighbor(v2, 5)

    print(v1, v1.id)
    print(next(v1.connect))
    print(v1.get_weight(v2))
