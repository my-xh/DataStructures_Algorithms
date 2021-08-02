# -*- coding: utf-8 -*-

from typing import Iterator

from pythonds.graphs.vertex import Vertex


class Graph:
    """图"""

    def __init__(self):
        self.__vertex_list = {}  # 顶点列表
        self.__num = 0  # 顶点数

    def __contains__(self, key):
        return key in self.__vertex_list

    def __iter__(self) -> Iterator[Vertex]:
        return iter(self.__vertex_list.values())

    @property
    def num_of_vertex(self):
        return self.__num

    def add_vertex(self, key) -> Vertex:
        if key not in self.__vertex_list:
            self.__vertex_list[key] = Vertex(key)
            self.__num += 1
        return self.__vertex_list[key]

    def add_edge(self, from_key, to_key, weight=0):
        from_vertex = self.add_vertex(from_key)
        to_vertex = self.add_vertex(to_key)
        from_vertex.add_neighbor(to_vertex, weight)

    def get_vertex(self, key) -> Vertex:
        vertex = None
        if key in self.__vertex_list:
            vertex = self.__vertex_list[key]

        return vertex

    def get_all_vertex(self):
        return list(self.__vertex_list.keys())


if __name__ == '__main__':
    g = Graph()
    for i in range(6):
        g.add_vertex(i)

    print(g.num_of_vertex)
    print(g.get_all_vertex())

    g.add_edge(0, 1, 5)
    g.add_edge(0, 5, 2)
    g.add_edge(1, 2, 4)
    g.add_edge(2, 3, 9)
    g.add_edge(3, 4, 7)
    g.add_edge(3, 5, 3)
    g.add_edge(4, 0, 1)
    g.add_edge(5, 2, 1)
    g.add_edge(5, 4, 8)

    print(0 in g)
    print(g.get_vertex(0))
    print(6 in g)
    print(g.get_vertex(6))

    for v in g:
        print(f'{v}')
        for w in v.connect:
            print(f'{v.id} -> {w.id}')
