import networkx as nx
import matplotlib.pyplot as plt

# G = nx.Graph()
# G.add_nodes_from(["B", "C", "D"])
# G.add_edges_from([("A", "C"), ("B", "C"), ("B", "D")])
# print(G.nodes())  # ['A', 'B', 'C', 'D']
# print(G.edges())  # [('A', 'B'), ('A', 'C'), ('B', 'C'), ('B', 'D')]

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