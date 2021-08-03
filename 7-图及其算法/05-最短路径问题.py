# -*- coding: utf-8 -*-

from pythonds.graphs import Graph, Vertex
from pythonds.priority_queue import PriorityQueue


# 构建路线图
def build_graph(g_map) -> Graph:
    g = Graph()
    for u in g_map:
        for v, w in g_map[u].items():
            g.add_edge(u, v, w)

    return g


# 初始化路线图
def init_graph(g: Graph):
    for vertex in g:
        vertex.distance = float('inf')
        vertex.predecessor = None


# Dijkstra最短路径算法
def dijkstra(g: Graph, start) -> Vertex:
    start_vertex = g.get_vertex(start)
    if start_vertex is None:
        raise ValueError(f'{start}点不存在')

    # 初始化
    init_graph(g)
    start_vertex.distance = 0

    queue = PriorityQueue()
    vertex_list = [(vertex, vertex.distance) for vertex in g]
    queue.build_queue(vertex_list)

    while not queue.is_empty():
        vertex: Vertex = queue.dequeue()
        for neighbor in vertex.connect:
            new_distance = vertex.distance + vertex.get_weight(neighbor)
            if new_distance < neighbor.distance:
                neighbor.distance = new_distance
                neighbor.predecessor = vertex
                queue.update_priority(neighbor, new_distance)

    return start_vertex


# 获取指定地点到其他地点的最短路径
def get_paths(g: Graph, start, verbose=False) -> dict[tuple, list[Vertex]]:
    start_vertex = dijkstra(g, start)

    paths = {}
    for vertex in g:
        path, end_vertex = [], vertex
        while vertex:
            path.append(vertex)
            vertex = vertex.predecessor
        paths[start_vertex.id, end_vertex.id] = path[::-1]

    if verbose:
        show_paths(paths)

    return paths


# 展示指定地点之间的最短路径
def show_path(paths, start, end):
    key = (start, end)
    if (path := paths.get(key)) is None:
        print(f'不存在 {start} 到 {end} 的路线')
        return

    end_vertex = path[-1]
    print(f'{start} 到 {end} 的距离: {end_vertex.distance}')
    print(f'路线: {" -> ".join(vertex.id for vertex in path)}')


# 展示所有最短路径
def show_paths(paths):
    for (start, end) in paths:
        show_path(paths, start, end)
        print('*' * 30)


if __name__ == '__main__':
    g_map = {
        'u': {
            'v': 2, 'w': 5, 'x': 1,
        },
        'v': {
            'u': 2, 'w': 3, 'x': 2,
        },
        'w': {
            'u': 5, 'v': 3, 'x': 3, 'y': 1, 'z': 5,
        },
        'x': {
            'u': 1, 'v': 2, 'w': 3, 'y': 1,
        },
        'y': {
            'w': 1, 'x': 1, 'z': 1,
        },
        'z': {
            'w': 5, 'y': 1,
        },
    }
    g = build_graph(g_map)
    start = 'u'
    end = 'z'
    paths = get_paths(g, start, verbose=True)
    show_path(paths, start, 'a')
    show_path(paths, start, end)
