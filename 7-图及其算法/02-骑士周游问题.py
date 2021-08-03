# -*- coding: utf-8 -*-
import time

from itertools import count

from pythonds.graphs import Graph, Vertex


def timeit(func):
    def wrapper(*args):
        start = time.time()
        res = func(*args)
        end = time.time()
        print(f'used: {end - start}s')
        return res

    return wrapper


# 将所有相邻顶点按可选走法数量从少到多排序
def order_by_avail(start_vertex: Vertex):
    vertex_list = []
    cnt = count()
    for vertex in start_vertex.connect:
        c = 0
        for neighbor in vertex.connect:
            if neighbor.color == 'white':
                c += 1
        vertex_list.append((c, next(cnt), vertex))
    vertex_list.sort()
    yield from (i[2] for i in vertex_list)


# 获取相邻顶点（可指定策略，默认顺序遍历）
def get_neighbors(vertex: Vertex, strategy=None):
    if strategy is None:
        yield from vertex.connect
    else:
        yield from strategy(vertex)


class Board:
    """棋盘"""

    def __init__(self, bd_size):
        self.board_size = bd_size
        self.g = self._build_graph()

    # 构建骑士周游图
    def _build_graph(self) -> Graph:
        g = Graph()
        for y in range(self.board_size):
            for x in range(self.board_size):
                for pos in self._next_position(x, y):
                    self._add_edge(g, (x, y), pos)

        return g

    # 在两个坐标点之间建立一条边
    def _add_edge(self, g: Graph, p1, p2):
        g.add_edge(self._convert2vertex(*p1), self._convert2vertex(*p2))

    # 将坐标转换成对应的顶点id
    def _convert2vertex(self, x, y):
        return y * self.board_size + x

    # 计算可以移动到的下一个位置
    def _next_position(self, x, y):
        direction = [
            (-2, 1), (-1, 2), (1, 2), (2, 1),
            (-2, -1), (-1, -2), (1, -2), (2, -1),
        ]
        yield from ((nx, ny) for dx, dy in direction
                    if self._in_board(nx := x + dx, ny := y + dy))

    # 判断坐标是否在棋盘内
    def _in_board(self, x, y):
        return 0 <= x < self.board_size and 0 <= y < self.board_size

    # 骑士周游
    @timeit
    def knight_tour(self, start_point):
        # 深度优先搜索
        def dfs(vertex: Vertex, i):
            vertex.color = 'gray'
            path.append(str(vertex.id))
            if i >= n:
                return True
            find = False
            for neighbor in get_neighbors(vertex, strategy=order_by_avail):
                if neighbor.color != 'white':
                    continue
                find = dfs(neighbor, i + 1)
                if find:
                    break
                path.pop()
                neighbor.color = 'white'

            return find

        vertex = self.g.get_vertex(start_point)
        n = self.g.num_of_vertex
        path = []
        dfs(vertex, 1)

        return path


if __name__ == '__main__':
    board = Board(8)
    path = board.knight_tour(4)
    print(' -> '.join(path))
