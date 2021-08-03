# -*- coding: utf-8 -*-

from random import choice
from collections import defaultdict, deque

from pythonds.graphs import Graph, Vertex
from pythonds.priority_queue import PriorityQueue


# 构建广播图
def build_graph(g_map) -> Graph:
    g = Graph()
    for u in g_map:
        for v, w in g_map[u].items():
            g.add_edge(u, v, w)
            g.add_edge(v, u, w)

    return g


# 初始化广播图
def init_graph(g: Graph):
    for vertex in g:
        vertex.distance = float('inf')
        vertex.predecessor = None


# Prim最小生成树算法
def prim(g: Graph):
    # 随机选择一个起始顶点
    start_vertex = g.get_vertex(choice(g.get_all_vertex()))
    # 初始化
    init_graph(g)
    start_vertex.distance = 0

    queue = PriorityQueue()
    vertex_list = [(vertex, vertex.distance) for vertex in g]
    queue.build_queue(vertex_list)

    while not queue.is_empty():
        vertex: Vertex = queue.dequeue()
        for neighbor in vertex.connect:
            if neighbor not in queue:
                continue
            new_cost = vertex.get_weight(neighbor)
            if new_cost < neighbor.distance:
                neighbor.distance = new_cost
                neighbor.predecessor = vertex
                queue.update_priority(neighbor, new_cost)


# 获取最小生成树（Minimum Spanning Tree）
def get_mst(g: Graph, verbose=False) -> tuple[Vertex, dict[Vertex, list[Vertex]]]:
    prim(g)

    root = None
    mst = defaultdict(list)
    for vertex in g:
        if vertex.predecessor is None:
            root = vertex
            continue
        mst[vertex.predecessor].append(vertex)

    if verbose:
        show_mst(root, mst)

    return root, mst


# 展示最小生成树
def show_mst(root, mst):
    print(f'The root of MST is "{root.id}"')
    queue = deque([root])
    while queue:
        u = queue.popleft()
        for v in mst.get(u, []):
            queue.append(v)
            print(f'{u.id}->{v.id}')


if __name__ == '__main__':
    g_map = {
        'A': {
            'B': 2, 'C': 3,
        },
        'B': {
            'C': 1, 'D': 1, 'E': 4,
        },
        'C': {
            'F': 5,
        },
        'D': {
            'E': 1,
        },
        'E': {
            'F': 1,
        },
        'F': {
            'G': 1,
        },
    }
    g = build_graph(g_map)
    get_mst(g, verbose=True)
