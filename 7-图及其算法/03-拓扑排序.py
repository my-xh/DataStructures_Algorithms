# -*- coding: utf-8 -*-

from pythonds.graphs import DFSGraph


# 外部实现拓扑排序[O(nlogn)]
def topo_sort(g: DFSGraph):
    g.dfs()
    ans = []
    for vertex in g:
        ans.append(vertex)
    ans.sort(key=lambda v: v.finish_time, reverse=True)
    return ans


if __name__ == '__main__':
    tasks = ['3/4杯牛奶', '一个鸡蛋', '一勺油', '一杯松饼粉', '加热平底锅',
             '倒入1/4杯', '出现气泡时翻面', '加热枫糖浆', '开始享用']
    g = DFSGraph()
    g.add_edge(tasks[0], tasks[3])
    g.add_edge(tasks[4], tasks[5])
    g.add_edge(tasks[1], tasks[3])
    g.add_edge(tasks[2], tasks[3])
    g.add_edge(tasks[3], tasks[5])
    g.add_edge(tasks[3], tasks[7])
    g.add_edge(tasks[5], tasks[6])
    g.add_edge(tasks[6], tasks[8])
    g.add_edge(tasks[7], tasks[8])
    task_list = topo_sort(g)
    print(' -> '.join(str(t.id) for t in task_list))

    # DFSGraph内置拓扑排序[O(n)]
    print(' -> '.join(str(v.id) for v in g.topo_sort()))
