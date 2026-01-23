# 2. Lưu đồ thị
import matplotlib 
import matplotlib.pyplot as plt
import networkx as nx

# Hàm lưu đồ thị dưới dạng hình ảnh PNG
def save_graph(graph, filename="graph.png"):
    plt.clf()
    plt.figure(figsize=(6, 4))
    pos = nx.spring_layout(graph.graph)

    # Vẽ đồ thị với các tùy chọn định dạng
    nx.draw(
        graph.graph, pos,
        with_labels=True,
        node_color="lightgreen",
        edge_color="black",
        node_size=800,
        font_size=10
    )
    # Vẽ nhãn trọng số cạnh nếu có
    edge_labels = nx.get_edge_attributes(graph.graph, 'weight')
    if edge_labels:
        nx.draw_networkx_edge_labels(graph.graph, pos, edge_labels=edge_labels)
    plt.savefig(filename, format="png", dpi=300)
    plt.close()

    print(f"Đã lưu đồ thị vào file: {filename}")
