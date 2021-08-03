# -*- coding: utf-8 -*-

from pythonds.graphs import DFSGraph


# 展示强连通分量(Strongly Connected Components)
def show_scc(g: DFSGraph):
    scc_mp = g.scc()
    for key, scc in scc_mp.items():
        print(f'scc_id: {key}')
        print(f'scc: [{" -> ".join(str(v.id) for v in scc)}]')
        print('*' * 30)


if __name__ == '__main__':
    g = DFSGraph()
    g.add_edge('A', 'B')
    g.add_edge('B', 'C')
    g.add_edge('B', 'E')
    g.add_edge('C', 'C')
    g.add_edge('C', 'F')
    g.add_edge('D', 'B')
    g.add_edge('D', 'G')
    g.add_edge('E', 'A')
    g.add_edge('E', 'D')
    g.add_edge('F', 'H')
    g.add_edge('G', 'E')
    g.add_edge('H', 'I')
    g.add_edge('I', 'F')
    show_scc(g)
