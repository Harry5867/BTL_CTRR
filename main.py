from graph import Graph
from visualize import visualize
from save import save_graph
from shortest_path import shortest_path
from traversal import bfs, dfs
from bipartite_check import is_bipartite
from conversion import convert_graph_demo
from algorithms_visualization import (
    ford_fulkerson,
    kruskal,
    prim,
    fleury,
    hierholzer
)


def input_graph():
    print("\n=== NHẬP ĐỒ THỊ MỚI ===")
    directed = input("Đồ thị có hướng? (y/n): ").strip().lower() == "y"
    g = Graph(directed=directed)

    try:
        m = int(input("Nhập số cạnh: "))
    except ValueError:
        print("Số cạnh phải là số nguyên!")
        return None

    print("Nhập các cạnh theo dạng: u v weight")

    for i in range(m):
        try:
            u, v, w = input(f"Cạnh {i+1}: ").split()
            g.add_edge(u, v, float(w))
        except ValueError:
            print("Sai định dạng! Ví dụ đúng: A B 4")
            return None

    print("Nhập đồ thị thành công!")
    return g


def require_graph(g):
    if not g:
        print("Bạn chưa nhập đồ thị!")
        return False
    return True

def main():
    g = None

    while True:
        print("\n========== MENU CHÍNH ==========")
        print("1. Nhập đồ thị mới")
        print("2. Vẽ đồ thị")
        print("3. Lưu đồ thị ra file PNG")
        print("4. Tìm đường đi ngắn nhất")
        print("5. Duyệt đồ thị (BFS & DFS)")
        print("6. Kiểm tra đồ thị 2 phía")
        print("7. Chuyển đổi biểu diễn đồ thị")
        print("8. Trực quan hóa thuật toán")
        print("0. Thoát")

        choice = input("Chọn chức năng: ").strip()

        # 1. Nhập đồ thị
        if choice == "1":
            g = input_graph()

        # 2. Vẽ đồ thị
        elif choice == "2":
            if require_graph(g):
                visualize(g)

        # 3. Lưu đồ thị
        elif choice == "3":
            if require_graph(g):
                save_graph(g, "graph.png")

        # 4. Đường đi ngắn nhất
        elif choice == "4":
            if require_graph(g):
                s = input("Đỉnh bắt đầu: ")
                t = input("Đỉnh kết thúc: ")
                shortest_path(g, s, t)

        # 5. BFS / DFS
        elif choice == "5":
            if require_graph(g):
                start = input("Đỉnh bắt đầu: ")
                bfs(g, start)
                dfs(g, start)

        # 6. Kiểm tra đồ thị 2 phía
        elif choice == "6":
            if require_graph(g):
                is_bipartite(g)

        # 7. Chuyển đổi biểu diễn
        elif choice == "7":
            if require_graph(g):
                convert_graph_demo(g)

        # 8. Trực quan thuật toán
        elif choice == "8":
            if not require_graph(g):
                continue

            print("\n--- CHỌN THUẬT TOÁN ---")
            print("1. Prim (MST)")
            print("2. Kruskal (MST)")
            print("3. Ford-Fulkerson (Max Flow)")
            print("4. Fleury (Euler Path)")
            print("5. Hierholzer (Euler Cycle)")

            ch = input("Chọn: ").strip()

            if ch == "1":
                prim(g)

            elif ch == "2":
                kruskal(g)

            elif ch == "3":
                if not g.directed:
                    print("Ford-Fulkerson yêu cầu đồ thị có hướng!")
                else:
                    s = input("Nguồn: ")
                    t = input("Đích: ")
                    ford_fulkerson(g, s, t)

            elif ch == "4":
                fleury(g)

            elif ch == "5":
                hierholzer(g)

            else:
                print("Lựa chọn không hợp lệ!")

        # 0. Thoát
        elif choice == "0":
            print("Thoát chương trình!")
            break

        else:
            print("Lựa chọn không hợp lệ!")


if __name__ == "__main__":
    main()
