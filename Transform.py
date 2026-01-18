from Graph import Graph

def adj_list_to_adj_matrix(graph):
    """
    Chuyển từ danh sách kề sang ma trận kề
    graph: đối tượng Graph (từ Graph.py)
    return: matrix, vertex_index
    """
    vertices = graph.get_vertices()
    n = len(vertices)

    # Gán chỉ số cho mỗi đỉnh
    index = {v: i for i, v in enumerate(vertices)}

    # Khởi tạo ma trận 0
    matrix = [[0] * n for _ in range(n)]

    for u in vertices:
        for v, w in graph.get_neighbors(u):
            i = index[u]
            j = index[v]
            matrix[i][j] = w

    return matrix, index


def adj_matrix_to_adj_list(matrix, vertices, directed=False, weighted=False):
    """
    Chuyển từ ma trận kề sang danh sách kề
    """
    graph = Graph(directed=directed, weighted=weighted)
    n = len(vertices)

    for i in range(n):
        graph.add_vertex(vertices[i])

    for i in range(n):
        for j in range(n):
            if matrix[i][j] != 0:
                graph.add_edge(vertices[i], vertices[j], matrix[i][j])

    return graph

def adj_list_to_edge_list(graph):
    return graph.get_edges()
def edge_list_to_adj_list(edges, directed=False, weighted=False):
    graph = Graph(directed=directed, weighted=weighted)
    for u, v, w in edges:
        graph.add_edge(u, v, w)
    return graph
