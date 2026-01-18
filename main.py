from Graph import Graph
from traversal import bfs, dfs
from Test import is_bipartite
from dijkstra import dijkstra, get_path
from convert import (
    adj_list_to_adj_matrix,
    adj_list_to_edge_list
)


def input_graph():
    print("\n=== NHẬP ĐỒ THỊ MỚI ===")
    directed = input("Đồ thị có hướng? (y/n): ").lower() == "y"
    weighted = input("Đồ thị có trọng số? (y/n): ").lower() == "y"

    g = Graph(directed=directed, weighted=weighted)

    m = int(input("Nhập số cạnh: "))
    print("Nhập các cạnh theo dạng: u v w")

    for _ in range(m):
        parts = input("Cạnh: ").split()
        u, v = parts[0], parts[1]
        w = float(parts[2]) if weighted else 1
        g.add_edge(u, v, w)

    print("Nhập đồ thị thành công!")
    return g


def menu():
    print("\n=== MENU CHÍNH ===")
    print("1. Nhập đồ thị mới")
    print("2. Hiển thị đồ thị (danh sách kề)")
    print("3. BFS")
    print("4. DFS")
    print("5. Tìm đường đi ngắn nhất")
    print("6. Kiểm tra đồ thị 2 phía")
    print("7. Chuyển sang ma trận kề")
    print("8. Chuyển sang danh sách cạnh")
    print("0. Thoát")


def main():
    g = None

    while True:
        menu()
        choice = input("Chọn chức năng: ")

        # 1. Nhập đồ thị
        if choice == "1":
            g = input_graph()

        # 2. Hiển thị đồ thị
        elif choice == "2":
            if g:
                print("\nDanh sách kề:")
                print(g)
            else:
                print("Chưa có đồ thị")

        # 3. BFS
        elif choice == "3":
            if g:
                start = input("Đỉnh bắt đầu BFS: ")
                print("BFS:", bfs(g, start))
            else:
                print("Chưa có đồ thị")

        # 4. DFS
        elif choice == "4":
            if g:
                start = input("Đỉnh bắt đầu DFS: ")
                print("DFS:", dfs(g, start))
            else:
                print("Chưa có đồ thị")

        # 5. Dijkstra
        elif choice == "5":
            if not g:
                print("Chưa có đồ thị")
                continue
            if not g.weighted:
                print("Dijkstra chỉ dùng cho đồ thị có trọng số")
                continue

            s = input("Đỉnh bắt đầu: ")
            t = input("Đỉnh kết thúc: ")
            dist, prev = dijkstra(g, s)
            print("Khoảng cách:", dist[t])
            print("Đường đi:", get_path(prev, s, t))

        # 6. Đồ thị hai phía
        elif choice == "6":
            if g:
                print("Đồ thị hai phía:", is_bipartite(g))
            else:
                print(" Chưa có đồ thị")

        # 7. Ma trận kề
        elif choice == "7":
            if g:
                matrix, index = adj_list_to_adj_matrix(g)
                print("Ma trận kề:")
                for row in matrix:
                    print(row)
            else:
                print("Chưa có đồ thị")

        # 8. Danh sách cạnh
        elif choice == "8":
            if g:
                edges = adj_list_to_edge_list(g)
                print("Danh sách cạnh:")
                for e in edges:
                    print(e)
            else:
                print("Chưa có đồ thị")

        # 0. Thoát
        elif choice == "0":
            print("Thoát chương trình.")
            break

        else:
            print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()
