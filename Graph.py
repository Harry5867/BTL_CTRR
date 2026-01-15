class Graph:
    """
    Lớp Graph biểu diễn đồ thị bằng danh sách kề (Adjacency List).
    Hỗ trợ:
    - Đồ thị có hướng / vô hướng
    - Đồ thị có trọng số / không trọng số
    """
    def __init__(self, directed=False, weighted=False):
        """
        Khởi tạo đồ thị.
        directed: True nếu đồ thị có hướng
        weighted: True nếu đồ thị có trọng số
        """
        self.directed = directed
        self.weighted = weighted
        self.adj_list = {}   # {vertex: [(neighbor, weight), ...]}

    # CÁC HÀM CƠ BẢN

    def add_vertex(self, v):
        """Thêm một đỉnh vào đồ thị nếu chưa tồn tại"""
        if v not in self.adj_list:
            self.adj_list[v] = []

    def add_edge(self, u, v, w=1):
        """
        Thêm một cạnh từ u đến v.
        Nếu đồ thị vô hướng thì thêm cả cạnh v đến u.
        """
        self.add_vertex(u)
        self.add_vertex(v)

        if not self.weighted:
            w = 1

        self.adj_list[u].append((v, w))

        if not self.directed:
            self.adj_list[v].append((u, w))


    # HÀM TRUY XUẤT THÔNG TIN

    def get_vertices(self):
        """Trả về danh sách các đỉnh."""
        return list(self.adj_list.keys())

    def get_neighbors(self, v):
        """Trả về danh sách các đỉnh kề của v."""
        return self.adj_list.get(v, [])

    def get_edges(self):
        """
        Trả về danh sách các cạnh của đồ thị.
        Mỗi cạnh có dạng (u, v, w)
        """
        edges = []
        visited = set()

        for u in self.adj_list:
            for v, w in self.adj_list[u]:
                if self.directed or (u, v) not in visited:
                    edges.append((u, v, w))
                    visited.add((v, u))
        return edges

    # HÀM KIỂM TRA

    def has_vertex(self, v):
        """Kiểm tra đỉnh có tồn tại hay không."""
        return v in self.adj_list

    def vertex_count(self):
        """Trả về số lượng đỉnh."""
        return len(self.adj_list)

    def edge_count(self):
        """Trả về số lượng cạnh."""
        return len(self.get_edges())

    # HIỂN THỊ & DEBUG

    def display(self):
        """In danh sách kề của đồ thị."""
        for v in self.adj_list:
            print(f"{v} -> {self.adj_list[v]}")

    def __str__(self):
        """In đồ thị khi gọi print(graph)."""
        result = ""
        for v in self.adj_list:
            result += f"{v} -> {self.adj_list[v]}\n"
        return result
