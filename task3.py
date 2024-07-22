import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

cities = [
    "Київ", "Харків", "Дніпро", "Одеса", "Запоріжжя", "Львів", "Кривий Ріг",
    "Миколаїв", "Вінниця", "Херсон", "Полтава", "Чернігів",
    "Черкаси", "Хмельницький", "Чернівці", "Житомир", "Суми", "Рівне",
    "Івано-Франківськ", "Тернопіль", "Луцьк", "Ужгород", "Донецьк", "Луганськ", "Сімферополь"
]
G.add_nodes_from(cities)

roads_with_weights = [
    ("Київ", "Харків", 1), ("Київ", "Житомир", 2), ("Київ",
                                                    "Дніпро", 3), ("Київ", "Одеса", 4), ("Київ", "Львів", 5),
    ("Київ", "Вінниця", 2), ("Київ", "Чернігів",
                             3), ("Київ", "Черкаси", 4), ("Харків", "Дніпро", 2),
    ("Дніпро", "Запоріжжя", 3), ("Дніпро", "Одеса", 4), ("Дніпро", "Кривий Ріг", 3),
    ("Одеса", "Миколаїв", 1), ("Запоріжжя",
                               "Донецьк", 2), ("Львів", "Хмельницький", 3),
    ("Львів", "Чернівці", 4), ("Львів", "Тернопіль",
                               3), ("Львів", "Луцьк", 5), ("Львів", "Ужгород", 6),
    ("Вінниця", "Хмельницький", 2), ("Вінниця",
                                     "Житомир", 2), ("Херсон", "Миколаїв", 2),
    ("Херсон", "Запоріжжя", 3), ("Полтава", "Харків", 2), ("Полтава", "Дніпро", 3),
    ("Чернігів", "Суми", 1), ("Черкаси", "Кіровоград", 3), ("Черкаси", "Полтава", 2),
    ("Чернівці", "Івано-Франківськ", 1), ("Житомир",
                                          "Рівне", 2), ("Суми", "Харків", 2),
    ("Рівне", "Луцьк", 1), ("Івано-Франківськ", "Тернопіль",
                            2), ("Донецьк", "Луганськ", 3), ("Сімферополь", "Херсон", 4)
]
G.add_weighted_edges_from(roads_with_weights)

def dijkstra_all_pairs(graph):
    paths = {}
    lengths = {}
    for node in graph.nodes:
        length, path = nx.single_source_dijkstra(graph, node)
        paths[node] = path
        lengths[node] = length
    return paths, lengths


all_paths, all_lengths = dijkstra_all_pairs(G)

print("Найкоротші шляхи між всіма парами міст:")
for start_node, paths in all_paths.items():
    for end_node, path in paths.items():
        print(f"Від {start_node} до {end_node}: шлях = {
              path}, довжина = {all_lengths[start_node][end_node]}")

plt.figure(figsize=(15, 10))
pos = nx.spring_layout(G, seed=42) 
labels = nx.get_edge_attributes(G, 'weight')
nx.draw(G, pos, with_labels=True, node_size=700,
        node_color="lightblue", font_size=10, font_weight="bold")
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("Транспортна мережа обласних центрів України з вагами")
plt.show()
