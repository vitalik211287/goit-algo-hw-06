# goit-algo-hw-06 | Домашнє завдання: Графи

import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
import heapq

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

# Завдання 2: Реалізація DFS і BFS

def dfs_recursive(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex)
    print(vertex, end=' ')
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

def bfs_recursive(graph, queue, visited=None):
    if visited is None:
        visited = set()
    if not queue:
        return
    vertex = queue.popleft()
    if vertex not in visited:
        print(vertex, end=" ")
        visited.add(vertex)
        queue.extend(set(graph[vertex]) - visited)
    bfs_recursive(graph, queue, visited)

print("\nDFS:", end=" ")
dfs_recursive(G, "A")

print("\nBFS:", end=" ")
bfs_recursive(G, deque(["A"]))

# Завдання 3: Реалізація алгоритму Дейкстри з таблицею

def print_table(distances, visited):
    print("\n")
    print("{:<10} {:<10} {:<10}".format("Вершина", "Відстань", "Перевірено"))
    print("-" * 30)
    for vertex in distances:
        distance = distances[vertex] if distances[vertex] != float('inf') else "∞"
        status = "Так" if vertex in visited else "Ні"
        print("{:<10} {:<10} {:<10}".format(vertex, distance, status))
    print("\n")

def dijkstra(graph, start):
    distances = {node: float("inf") for node in graph.nodes()}
    distances[start] = 0
    visited = set()
    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_node in visited:
            continue
        visited.add(current_node)

        for neighbor in graph.neighbors(current_node):
            weight = graph[current_node][neighbor]['weight']
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

        print_table(distances, visited)

    return distances

shortest_paths = dijkstra(G, "A")
print("Найкоротші відстані від вузла A:")
for target, distance in shortest_paths.items():
    print(f"До {target}: {distance}")
