# 1. Vẽ đồ thị trực quan
import matplotlib.pyplot as plt
import networkx as nx

# Hàm để vẽ đồ thị
def visualize(graph):
    pos = nx.spring_layout(graph.graph)

    # Lấy trọng số tất cả các cạnh
    weights = nx.get_edge_attributes(graph.graph, 'weight')

    # Vẽ đồ thị nền
    nx.draw(graph.graph, pos, with_labels=True, node_color='lightblue', node_size=800)
    
    # Vẽ các cạnh thuật toán
    nx.draw_networkx_edge_labels(graph.graph, pos, edge_labels=weights)
    
    # Vẽ nhãn trọng số cho tất cả các cạnh
    nx.draw_networkx_edge_labels(graph.graph, pos, edge_labels=weights)
     
    plt.show()