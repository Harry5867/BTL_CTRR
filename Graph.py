import networkx as nx

class Graph:
    def __init__(self, directed=False):
        self.directed = directed
        self.graph = nx.DiGraph() if directed else nx.Graph()

    def add_edge(self, u, v, weight=1):
        self.graph.add_edge(u, v, weight=weight)

    def nodes(self):
        return list(self.graph.nodes)

    def edges(self):
        return list(self.graph.edges(data=True))
