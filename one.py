import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


# Завдання 1: Створення графа транспортної мережі
G = nx.Graph()

# Додаємо вузли (міста або станції)
cities = ["A", "B", "C", "D", "E", "F"]
G.add_nodes_from(cities)

# Додаємо ребра (дороги між містами)
roads = [
    ("A", "B", 5),
    ("A", "C", 7),
    ("B", "D", 3),
    ("C", "D", 2),
    ("D", "E", 4),
    ("E", "F", 6),
    ("C", "F", 10)
]
G.add_weighted_edges_from(roads)

# Візуалізація графа
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=700, font_weight='bold')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("Транспортна мережа")
plt.show()

# Аналіз графа
print("Кількість вершин:", G.number_of_nodes())
print("Кількість ребер:", G.number_of_edges())
print("Ступені вершин:")
for node in G.nodes():
    print(f"{node}: {G.degree(node)}")

    # Завдання 2

def dfs_recursive(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex)
    print(vertex, end=' ')  # Відвідуємо вершину
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)


def bfs_recursive(graph, queue, visited=None):
    # Перевіряємо, чи існує множина відвіданих вершин, якщо ні, то ініціалізуємо нову
    if visited is None:
        visited = set()
    # Якщо черга порожня, завершуємо рекурсію
    if not queue:
        return
    # Вилучаємо вершину з початку черги
    vertex = queue.popleft()
    # Перевіряємо, чи відвідували раніше дану вершину
    if vertex not in visited:
        # Якщо не відвідували, друкуємо вершину
        print(vertex, end=" ")
        # Додаємо вершину до множини відвіданих вершин.
        visited.add(vertex)
        # Додаємо невідвіданих сусідів даної вершини в кінець черги.
        queue.extend(set(graph[vertex]) - visited)
    # Рекурсивний виклик функції з тією ж чергою та множиною відвіданих вершин
    bfs_recursive(graph, queue, visited)

# print("DFS:", dfs_recursive(G, "A"))
# print("BFS:", bfs_recursive(G, deque(["A"])))

# dfs_recursive(G, "A", visited=None)
# bfs_recursive(G, deque(["A"]), visited=None)

print("\nDFS:", end=" ")
dfs_recursive(G, "A")

# print("\nBFS (ітеративно):", bfs(G, "A"))

print("\nBFS:", end=" ")
bfs_recursive(G, deque(["A"]))