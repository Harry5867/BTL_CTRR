# 6. Chuyển đổi qua lại giữa các phương pháp biểu diễn đồ thị
# Hàm chuyển ma trận kề sang danh sách kề
def adjacency_matrix_to_list(matrix, nodes, keep_weight=True):
    adj_list = {node: [] for node in nodes}
    for i, u in enumerate(nodes):
        for j, v in enumerate(nodes):
            if matrix[i][j] != 0:
                if keep_weight:
                    adj_list[u].append((v, matrix[i][j]))
                else:
                    adj_list[u].append(v)
    return adj_list

# Hàm chuyển danh sách kề sang ma trận kề
def list_to_matrix(adj_list):
    nodes = list(adj_list.keys())
    size = len(nodes)
    matrix = [[0]*size for _ in range(size)]
    for i, u in enumerate(nodes):
        for item in adj_list[u]:
            if isinstance(item, tuple):
                v, w = item
            else:
                v, w = item, 1
            j = nodes.index(v)
            matrix[i][j] = w
    return matrix

# Hàm chuyển danh sách kề sang danh sách cạnh
def adjacency_list_to_edge_list(adj_list, keep_weight=True):
    edges = []
    for u, neighbors in adj_list.items():
        for item in neighbors:
            if keep_weight:
                v, w = item
                edges.append((u, v, w))
            else:
                edges.append((u, item))
    return edges

# Hàm chuyển danh sách cạnh sang danh sách kề
def convert_graph_demo(graph):
    nodes = graph.nodes()
    size = len(nodes)

    # Tạo ma trận kề
    matrix = [[0]*size for _ in range(size)]
    for u, v, data in graph.edges():
        i = nodes.index(u)
        j = nodes.index(v)
        w = data.get('weight', 1)
        matrix[i][j] = w
        if not graph.directed:
            matrix[j][i] = w  # đối với đồ thị vô hướng

    # In ma trận kề
    print("=== Ma trận kề ===")
    print("    " + "  ".join(nodes))
    for i, u in enumerate(nodes):
        row = "  ".join(str(matrix[i][j]) for j in range(size))
        print(f"{u}: {row}")

    # Ma trận kề -> danh sách kề có trọng số
    adj_list = adjacency_matrix_to_list(matrix, nodes, keep_weight=True)
    print("\n=== Danh sách kề ===")
    for u, neighbors in adj_list.items():
        print(f"{u}: {neighbors}")

    # Danh sách kề -> danh sách cạnh có trọng số
    edges = adjacency_list_to_edge_list(adj_list, keep_weight=True)
    print("\n=== Danh sách cạnh ===")
    for u, v, w in edges:
        print(f"{u} -> {v}, weight = {w}")
