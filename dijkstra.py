import heapq
import math
from Graph import Graph

def dijkstra(graph, start):
    """
    Tìm đường đi ngắn nhất từ đỉnh start đến các đỉnh còn lại
    graph: đối tượng Graph (weighted=True)
    start: đỉnh bắt đầu
    """

    if not graph.weighted:
        raise ValueError("Dijkstra chỉ áp dụng cho đồ thị có trọng số")

    if not graph.has_vertex(start):
        raise ValueError("Đỉnh bắt đầu không tồn tại")

    # Khởi tạo khoảng cách
    dist = {v: math.inf for v in graph.get_vertices()}
    prev = {v: None for v in graph.get_vertices()}
    dist[start] = 0

    # Hàng đợi ưu tiên
    pq = [(0, start)]

    while pq:
        current_dist, u = heapq.heappop(pq)

        if current_dist > dist[u]:
            continue

        for v, w in graph.get_neighbors(u):
            new_dist = dist[u] + w

            if new_dist < dist[v]:
                dist[v] = new_dist
                prev[v] = u
                heapq.heappush(pq, (new_dist, v))

    return dist, prev


def get_path(prev, start, end):
    """
    Truy vết đường đi từ start đến end
    """
    path = []
    cur = end

    while cur is not None:
        path.append(cur)
        cur = prev[cur]

    path.reverse()

    if path and path[0] == start:
        return path
    return []


# ================== TEST NHANH ==================
if __name__ == "__main__":
    g = Graph(directed=False, weighted=True)

    g.add_edge("A", "B", 4)
    g.add_edge("A", "C", 2)
    g.add_edge("B", "C", 5)
    g.add_edge("B", "D", 10)
    g.add_edge("C", "E", 3)
    g.add_edge("E", "D", 4)

    dist, prev = dijkstra(g, "A")

    print("Khoảng cách ngắn nhất từ A:")
    for v in dist:
        print(f"A -> {v} = {dist[v]}")

    print("Đường đi từ A đến D:", get_path(prev, "A", "D"))

