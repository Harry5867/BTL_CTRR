from Graph import Graph

# CHUYỂN ĐỔI BIỂU DIỄN ĐỒ THỊ

def adj_list_to_adj_matrix(graph):
    """
    Chuyển từ danh sách kề sang ma trận kề
    Trả về: matrix, index (đỉnh -> chỉ số)
    """
    vertices = graph.get_vertices()
    n = len(vertices)

    index = {v: i for i, v in enumerate(vertices)}
    matrix = [[0] * n for _ in range(n)]

    for u in vertices:
        for v, w in graph.get_neighbors(u):
            i = index[u]
            j = index[v]
            matrix[i][j] = w if graph.weighted else 1

    return matrix, index


def adj_matrix_to_adj_list(matrix, vertices, directed=False, weighted=False):
    """
    Chuyển từ ma trận kề sang danh sách kề
    """
    graph = Graph(directed=directed, weighted=weighted)
    n = len(vertices)

    for v in vertices:
        graph.add_vertex(v)

    for i in range(n):
        for j in range(n):
            if matrix[i][j] != 0:
                if directed or j > i:
                    if weighted:
                        graph.add_edge(vertices[i], vertices[j], matrix[i][j])
                    else:
                        graph.add_edge(vertices[i], vertices[j])

    return graph


def adj_list_to_edge_list(graph):
    """
    Chuyển danh sách kề -> danh sách cạnh
    """
    return graph.get_edges()


def edge_list_to_adj_list(edges, directed=False, weighted=False):
    """
    Chuyển danh sách cạnh -> danh sách kề (Graph)
    """
    graph = Graph(directed=directed, weighted=weighted)

    for edge in edges:
        if weighted:
            u, v, w = edge
            graph.add_edge(u, v, w)
        else:
            u, v = edge[:2]
            graph.add_edge(u, v)

    return graph
