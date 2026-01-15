
from collections import deque
from Graph import Graph

# --------- 1. KIỂM TRA LIÊN THÔNG ---------

def is_connected(graph):
    """
    Kiểm tra đồ thị VÔ HƯỚNG có liên thông hay không
    """
    if graph.directed:
        raise ValueError("is_connected chỉ dùng cho đồ thị vô hướng")

    vertices = graph.get_vertices()
    if not vertices:
        return True

    visited = set()
    q = deque([vertices[0]])
    visited.add(vertices[0])

    while q:
        u = q.popleft()
        for v, _ in graph.get_neighbors(u):
            if v not in visited:
                visited.add(v)
                q.append(v)

    return len(visited) == graph.vertex_count()


# --------- 2. KIỂM TRA ĐỒ THỊ HAI PHÍA ---------

def is_bipartite(graph):
    """
    Kiểm tra đồ thị có phải là đồ thị hai phía không
    Dùng BFS + tô màu
    """
    color = {}

    for start in graph.get_vertices():
        if start in color:
            continue

        color[start] = 0
        q = deque([start])

        while q:
            u = q.popleft()
            for v, _ in graph.get_neighbors(u):
                if v not in color:
                    color[v] = 1 - color[u]
                    q.append(v)
                elif color[v] == color[u]:
                    return False

    return True

# --------- 3. KIỂM TRA CHU TRÌNH ---------

def has_cycle_undirected(graph):
    """
    Kiểm tra chu trình trong đồ thị vô hướng
    DFS + parent
    """
    visited = set()

    def dfs(u, parent):
        visited.add(u)
        for v, _ in graph.get_neighbors(u):
            if v not in visited:
                if dfs(v, u):
                    return True
            elif v != parent:
                return True
        return False

    for v in graph.get_vertices():
        if v not in visited:
            if dfs(v, None):
                return True

    return False
    