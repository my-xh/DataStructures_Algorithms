# -*- coding: utf-8 -*-

from pythonds.graphs.adjoin_graph import Graph


class DFSGraph(Graph):
    """
    深度优先搜索图

    支持的操作：

    DFS、拓扑排序、计算强连通分量
    """

    def __init__(self):
        super().__init__()
        self.time = 0
        self.__sort_list = []
        self.__scc_list = []

    def _initial_visit(self):
        """初始化图的访问信息"""
        self.time = 0
        self.__sort_list = []
        self.__scc_list = []
        for vertex in self:
            vertex.color = 'white'
            vertex.predecessor = None

    def _dfs(self, vertex):
        """深度优先搜索（递归实现）"""
        # 首次访问当前顶点
        self.time += 1
        vertex.color = 'gray'
        vertex.discovery_time = self.time

        # 尝试访问当前顶点的所有邻接顶点
        for neighbor in vertex.connect:
            if neighbor.color == 'white':
                neighbor.predecessor = vertex
                self._dfs(neighbor)

        # 结束当前顶点的访问
        self.time += 1
        vertex.color = 'black'
        vertex.finish_time = self.time
        # 按访问结束时间递增的顺序添加节点
        self.__sort_list.append(vertex)
        self.__scc_list[-1].append(vertex)

    def _transpose(self) -> "DFSGraph":
        """获得转置图"""
        gt = DFSGraph()
        for vertex in self:
            for neighbor in vertex.connect:
                gt.add_edge(neighbor.id, vertex.id)

        return gt

    def dfs(self, vertex_list=None):
        """
        深度优先搜索调用接口

        Args:
            vertex_list: 指定顶点遍历顺序
        Returns:
            None
        """
        # 初始化
        self._initial_visit()
        if vertex_list is None:
            vertex_list = self
        # 遍历所有顶点，对没有访问过的顶点递归调用_dfs
        for vertex in vertex_list:
            if vertex.color == 'white':
                self.__scc_list.append(list())
                self._dfs(vertex)

    def topo_sort(self):
        """
        拓扑排序调用接口

        Returns:
            拓扑排序后的顶点列表
        """
        # 进行深度优先搜索
        self.dfs()
        # 按访问结束时间递减的顺序返回结果
        self.__sort_list.reverse()
        return self.__sort_list

    def scc(self):
        """
        计算强连通分量调用接口

        Returns:
            强连通分量映射（id-顶点列表）
        """
        # 对图G进行拓扑排序
        topo = self.topo_sort()
        # 获得图G的转置图GT
        gt: DFSGraph = self._transpose()
        # 将图GT的顶点按图G的拓扑顺序进行排序
        for vid, vertex in enumerate(topo):
            topo[vid] = gt.get_vertex(vertex.id)
        # 对图GT进行深度优先搜素，顶点遍历顺序为图G的拓扑顺序
        gt.dfs(topo)
        # 提取强连通分量
        scc_mp = {}
        for scc in gt.__scc_list:
            value = scc[::-1]
            key = ''.join(str(v.id) for v in value)
            scc_mp[key] = value

        return scc_mp


if __name__ == '__main__':
    g = DFSGraph()
    g.add_edge('A', 'B')
    g.add_edge('A', 'D')
    g.add_edge('B', 'C')
    g.add_edge('B', 'D')
    g.add_edge('D', 'E')
    g.add_edge('E', 'B')
    g.add_edge('E', 'F')
    g.dfs()
    for v in g:
        print(v)
