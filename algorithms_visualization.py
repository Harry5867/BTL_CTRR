import networkx as nx
import matplotlib.pyplot as plt
from graph import Graph


def visualize_algorithm(graph: Graph, edges=None, title="Đồ thị"):
    G = graph.graph
    pos = nx.spring_layout(G, seed=42)

    nx.draw(
        G, pos,
        with_labels=True,
        node_color='lightblue',
        node_size=1500,
        edge_color='gray',
        width=2,
        font_size=13
    )

    if edges:
        nx.draw_networkx_edges(
            G, pos,
            edgelist=edges,
            edge_color='red',
            width=3
        )

    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.title(title)
    plt.show()


# PRIM
def prim(graph: Graph):
    if graph.directed:
        print("Prim chỉ áp dụng cho đồ thị vô hướng!")
        return

    if graph.graph.number_of_edges() == 0:
        print("Đồ thị không có cạnh!")
        return

    mst = list(nx.minimum_spanning_edges(graph.graph, algorithm="prim", data=True))
    total = sum(d["weight"] for _, _, d in mst)

    print("\n=== Prim MST ===")
    for u, v, d in mst:
        print(f"{u} - {v} (w = {d['weight']})")
    print("Tổng trọng số =", total)

    visualize_algorithm(graph, [(u, v) for u, v, _ in mst],
                        f"Prim (Total = {total})")


# KRUSKAL 
def kruskal(graph: Graph):
    if graph.directed:
        print("Kruskal chỉ áp dụng cho đồ thị vô hướng!")
        return

    mst = list(nx.minimum_spanning_edges(graph.graph, algorithm="kruskal", data=True))
    total = sum(d["weight"] for _, _, d in mst)

    print("\n=== Kruskal MST ===")
    for u, v, d in mst:
        print(f"{u} - {v} (w = {d['weight']})")
    print("Tổng trọng số =", total)

    visualize_algorithm(graph, [(u, v) for u, v, _ in mst],
                        f"Kruskal (Total = {total})")


#  FORD–FULKERSON 
def ford_fulkerson(graph: Graph, source, sink):
    if not graph.directed:
        print("Ford-Fulkerson yêu cầu đồ thị có hướng!")
        return

    G = graph.graph
    if source not in G or sink not in G:
        print("Nguồn hoặc đích không tồn tại!")
        return

    Gf = nx.DiGraph()
    for u, v, d in G.edges(data=True):
        cap = d.get("weight", 1)
        Gf.add_edge(u, v, capacity=cap)

    max_flow, flow = nx.maximum_flow(Gf, source, sink)

    print("\n=== Ford-Fulkerson ===")
    print("Max Flow =", max_flow)

    flow_edges = [
        (u, v)
        for u in flow
        for v in flow[u]
        if flow[u][v] > 0 and G.has_edge(u, v)
    ]

    visualize_algorithm(graph, flow_edges,
                        f"Ford-Fulkerson (Max Flow = {max_flow})")


#  FLEURY 
def fleury(graph: Graph):
    if graph.directed:
        print("Fleury chỉ dùng cho đồ thị vô hướng!")
        return

    G = graph.graph
    if not nx.has_eulerian_path(G):
        print("Đồ thị không có đường Euler!")
        return

    path = list(nx.eulerian_path(G))
    nodes = [path[0][0]] + [v for _, v in path]

    print("\n=== Fleury (Euler Path) ===")
    print(" -> ".join(nodes))

    visualize_algorithm(graph, list(zip(nodes, nodes[1:])),
                        "Fleury – Euler Path")


#  HIERHOLZER 
def hierholzer(graph: Graph):
    if graph.directed:
        print("Hierholzer chỉ dùng cho đồ thị vô hướng!")
        return

    G = graph.graph
    if not nx.is_eulerian(G):
        print("Đồ thị không có chu trình Euler!")
        return

    circuit = list(nx.eulerian_circuit(G))
    nodes = [circuit[0][0]] + [v for _, v in circuit]

    print("\n=== Hierholzer (Euler Cycle) ===")
    print(" -> ".join(nodes))

    visualize_algorithm(graph, list(zip(nodes, nodes[1:])),
                        "Hierholzer – Euler Cycle")
