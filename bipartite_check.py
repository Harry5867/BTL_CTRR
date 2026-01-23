# 5. Kiểm tra một đồ thị có phải là đồ thị 2 phía không?
import networkx as nx
import matplotlib.pyplot as plt

# Hàm kiểm tra đồ thị 2 phía và vẽ đồ thị
def is_bipartite(graph):
    G = graph.graph
    try:
        # Kiểm tra đồ thị 2 phía và trả về tập node cho mỗi phía nếu đúng
        is_bipart = nx.is_bipartite(G)
        if is_bipart:
            print("Đồ thị 2 phía!")
            # Lấy tập node của hai phía
            left_nodes, right_nodes = nx.bipartite.sets(G)

            # Vẽ đồ thị
            pos = nx.spring_layout(G, seed=42)
            nx.draw(G, pos,
                    with_labels=True,
                    node_color=["lightblue" if n in left_nodes else "salmon" for n in G.nodes],
                    node_size=1500,
                    font_size=13,
                    edge_color="gray",
                    width=2)
            plt.title("Đồ thị 2 phía")
            plt.show()

        else:
            print("Không phải đồ thị 2 phía!")

            # Thử tô 2 màu để phát hiện các đỉnh vi phạm
            color_map = {}
            highlight_nodes = set()

            for node in G.nodes:
                if node not in color_map:
                    # Dùng BFS để đánh màu
                    queue = [node]
                    color_map[node] = 0  # 0 = xanh, 1 = đỏ
                    while queue:
                        current = queue.pop(0)
                        for neighbor in G.neighbors(current):
                            if neighbor not in color_map:
                                color_map[neighbor] = 1 - color_map[current]
                                queue.append(neighbor)
                            else:
                                # Nếu cùng màu với neighbor → vi phạm
                                if color_map[neighbor] == color_map[current]:
                                    highlight_nodes.add(current)
                                    highlight_nodes.add(neighbor)

            # Vẽ đồ thị với 2 màu và nổi bật các đỉnh vi phạm
            pos = nx.spring_layout(G, seed=42)
            node_colors = []
            for n in G.nodes:
                if n in highlight_nodes:
                    node_colors.append("gold")  # Nổi bật đỉnh vi phạm
                else:
                    node_colors.append("lightblue" if color_map[n] == 0 else "salmon")

            nx.draw(G, pos,
                    with_labels=True,
                    node_color=node_colors,
                    node_size=1500,
                    font_size=13,
                    edge_color="gray",
                    width=2)
            plt.title("Không phải đồ thị 2 phía (đỉnh vi phạm màu vàng)")
            plt.show()

        return is_bipart

    except Exception as e:
        print("Lỗi kiểm tra đồ thị 2 phía:", e)
