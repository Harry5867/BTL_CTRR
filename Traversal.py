# 4. Duyệt BFS, DFS
import networkx as nx
import matplotlib.pyplot as plt

# Danh sách màu cho các đỉnh được duyệt theo thứ tự
colors_sequence = ["gold", "lightgreen", "skyblue", "orange", "violet", "pink", "cyan", "magenta"]

# Hàm duyệt BFS
def bfs(graph, start):
    G = graph.graph
    try:
        bfs_tree = nx.bfs_tree(G, source=start)
        visited = list(bfs_tree.nodes)
        edges = list(bfs_tree.edges)

        print("Duyệt BFS:", visited)

        pos = nx.spring_layout(G, seed=42)

        # Vẽ toàn bộ đồ thị nền
        nx.draw(
            G, pos,
            with_labels=False,
            node_color="lightgray",
            node_size=1500,
            font_size=13,
            edge_color="gray",
            width=2
        )

        # Tô các node theo thứ tự duyệt với màu khác nhau
        for i, node in enumerate(visited):
            nx.draw_networkx_nodes(
                G, pos,
                nodelist=[node],
                node_color=colors_sequence[i % len(colors_sequence)],
                node_size=1500
            )

        # Tạo nhãn node kèm số thứ tự duyệt
        labels_with_order = {node: f"{node}({i+1})" for i, node in enumerate(visited)}
        nx.draw_networkx_labels(G, pos, labels=labels_with_order, font_size=13, font_weight="bold")

        # Vẽ cạnh theo BFS
        nx.draw_networkx_edges(
            G, pos,
            edgelist=edges,
            edge_color="red",
            width=3
        )

        # Trọng số cạnh
        edge_labels = nx.get_edge_attributes(G, "weight")
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

        plt.title(f"Duyệt BFS từ {start}")
        plt.show()
        return visited
    
    # Xử lý ngoại lệ
    except Exception as e:
        print("Lỗi BFS:", e)

# Hàm duyệt DFS
def dfs(graph, start):
    G = graph.graph
    try:
        dfs_tree = nx.dfs_tree(G, source=start)
        visited = list(dfs_tree.nodes)
        edges = list(dfs_tree.edges)

        print("Duyệt DFS:", visited)

        pos = nx.spring_layout(G, seed=42)

        # Vẽ toàn đồ thị nền
        nx.draw(
            G, pos,
            with_labels=False,
            node_color="lightgray",
            node_size=1500,
            font_size=13,
            edge_color="gray",
            width=2
        )

        # Tô node theo thứ tự duyệt với màu khác nhau
        for i, node in enumerate(visited):
            nx.draw_networkx_nodes(
                G, pos,
                nodelist=[node],
                node_color=colors_sequence[i % len(colors_sequence)],
                node_size=1500
            )

        # Tạo nhãn node kèm số thứ tự duyệt
        labels_with_order = {node: f"{node}({i+1})" for i, node in enumerate(visited)}
        nx.draw_networkx_labels(G, pos, labels=labels_with_order, font_size=13, font_weight="bold")

        # Vẽ cạnh DFS
        nx.draw_networkx_edges(
            G, pos,
            edgelist=edges,
            edge_color="red",
            width=3
        )

        # Trọng số cạnh
        edge_labels = nx.get_edge_attributes(G, "weight")
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

        plt.title(f"Duyệt DFS từ {start}")
        plt.show()
        return visited
    # Xử lý ngoại lệ
    except Exception as e:
        print("Lỗi DFS:", e)
