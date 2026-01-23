# 3. Tìm đường đi ngắn nhất
import networkx as nx
import matplotlib.pyplot as plt

# Hàm tìm đường đi ngắn nhất và vẽ đồ thị với đường đi được tô đỏ
def shortest_path(graph, start, end):
    try:
        G = graph.graph

        # 1. Tìm đường đi ngắn nhất
        path = nx.shortest_path(G, source=start, target=end, weight='weight')
        length = nx.shortest_path_length(G, source=start, target=end, weight='weight')

        print(f"Đường đi ngắn nhất từ {start} -> {end}: {path}, độ dài = {length}")

        # 2. Tọa độ
        pos = nx.spring_layout(G, seed=42)

        # 3. Cạnh thuộc đường đi
        path_edges = list(zip(path, path[1:]))

        # 4. Vẽ đồ thị bình thường (màu lightblue)
        nx.draw(
            G, pos,
            with_labels=True,
            node_color="lightblue", 
            node_size=1500,
            font_size=13,
            edge_color="gray",
            width=2
        )

        # 5. Tô đỏ đường đi ngắn nhất
        nx.draw_networkx_edges(
            G, pos,
            edgelist=path_edges,
            edge_color="red",
            width=3
        )

        # 6. Thêm trọng số lên cạnh
        edge_labels = nx.get_edge_attributes(G, "weight")
        nx.draw_networkx_edge_labels(
            G, pos,
            edge_labels=edge_labels,
            font_color="black",
            font_size=11
        )
        plt.title(f"Đường đi ngắn nhất từ {start} đến {end}")
        plt.show()

    # Xử lý ngoại lệ
    except nx.NetworkXNoPath:
        print("Không tồn tại đường đi.")
    except Exception as e:
        print("Lỗi:", e)
