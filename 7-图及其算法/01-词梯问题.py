# -*- coding: utf-8 -*-

from collections import defaultdict

from pythonds.basic import Queue
from pythonds.graphs import Graph, Vertex

WORD_FILE = 'words.txt'


# 构建单词关系图
def build_graph(word_file) -> Graph:
    g = Graph()
    bucket = defaultdict(list)

    with open(word_file) as f:
        for line in f:
            word = line.strip()
            for i in range(len(word)):
                key = word[:i] + '_' + word[i + 1:]  # 下划线表示通配符
                bucket[key].append(word)  # 将只有一个字母不同的单词放入同一个桶中

    # 将同一个桶中的所有单词进行连接
    for words in bucket.values():
        for i in range(n := len(words)):
            word = words[i]
            for j in range(i + 1, n):
                other = words[j]
                g.add_edge(word, other, 1)
                g.add_edge(other, word, 1)

    return g


# 广度优先搜索
def bfs(g: Graph, start, end) -> int:
    start_vertex = g.get_vertex(start)
    end_vertex = g.get_vertex(end)
    if start_vertex is None or end_vertex is None:
        raise ValueError(f'{start}或{end}不在单词表中')

    queue, found = Queue(), False
    queue.enqueue(start_vertex)

    while not queue.is_empty() and not found:
        vertex: Vertex = queue.dequeue()
        for neighbor in vertex.connect:
            if neighbor.color == 'white':
                neighbor.color = 'gray'
                neighbor.predecessor = vertex
                neighbor.distance = vertex.distance + vertex.get_weight(neighbor)
                queue.enqueue(neighbor)
            # 找到目标时提前退出
            # if neighbor is end_vertex:
            #     found = True
        vertex.color = 'black'

    return end_vertex.distance


# 回溯最短路径
def traversal(g: Graph, end) -> list:
    res = []
    vertex = g.get_vertex(end)
    while vertex:
        res.append(vertex.id)
        vertex = vertex.predecessor

    return res


if __name__ == '__main__':
    g = build_graph(WORD_FILE)
    start, end = 'FOOL', 'SAGE'
    distance = bfs(g, start, end)
    print(f'the distance from {start} to {end} is: {distance}')
    trace = traversal(g, end)
    print(' -> '.join(trace[::-1]))
