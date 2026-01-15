from collections import deque

# =========================
# BFS – Breadth First Search
# Duyệt đồ thị theo chiều rộng
# Sử dụng hàng đợi (queue)
# =========================
def bfs(graph, start):
    # Kiểm tra đỉnh bắt đầu có tồn tại trong đồ thị không
    if not graph.has_vertex(start):
        return []

    visited = set()              # Lưu các đỉnh đã được thăm
    queue = deque([start])       # Hàng đợi phục vụ BFS
    result = []                  # Lưu thứ tự duyệt các đỉnh

    visited.add(start)

    # Lặp cho đến khi hàng đợi rỗng
    while queue:
        u = queue.popleft()      # Lấy đỉnh đầu hàng đợi
        result.append(u)         # Thêm vào kết quả duyệt

        # Duyệt các đỉnh kề của u
        for v, _ in graph.get_neighbors(u):
            if v not in visited:
                visited.add(v)   # Đánh dấu đã thăm
                queue.append(v)  # Đưa vào hàng đợi

    return result


# =========================
# DFS – Depth First Search
# Duyệt đồ thị theo chiều sâu
# Sử dụng đệ quy
# =========================
def dfs(graph, start):
    # Kiểm tra đỉnh bắt đầu có tồn tại trong đồ thị không
    if not graph.has_vertex(start):
        return []

    visited = set()              # Lưu các đỉnh đã được thăm
    result = []                  # Lưu thứ tự duyệt các đỉnh

    # Hàm đệ quy hỗ trợ DFS
    def dfs_util(u):
        visited.add(u)           # Đánh dấu đỉnh u đã thăm
        result.append(u)         # Thêm u vào kết quả

        # Duyệt các đỉnh kề của u
        for v, _ in graph.get_neighbors(u):
            if v not in visited:
                dfs_util(v)      # Gọi đệ quy cho đỉnh chưa thăm

    dfs_util(start)
    return result
