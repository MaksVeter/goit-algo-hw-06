import heapq
import matplotlib.pyplot as plt
import networkx as nx

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



def dijkstra(graph, start):
    shortest_paths = {node: (float('inf'), []) for node in graph.nodes}
    shortest_paths[start] = (0, [start])
    visited = set()
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_node in visited:
            continue

        visited.add(current_node)

        for neighbor, data in graph[current_node].items():
            distance = data['weight']
            total_distance = current_distance + distance

            if total_distance < shortest_paths[neighbor][0]:
                shortest_paths[neighbor] = (
                    total_distance, shortest_paths[current_node][1] + [neighbor])
                heapq.heappush(priority_queue, (total_distance, neighbor))

    return shortest_paths


all_shortest_paths = {city: dijkstra(G, city) for city in cities}

for start_city in cities:
    print(f"Найкоротші шляхи з {start_city}:")
    for end_city, (dist, path) in all_shortest_paths[start_city].items():
        print(f"До {end_city}: шлях = {path}, довжина = {dist}")
    print()

plt.figure(figsize=(15, 10))
pos = nx.spring_layout(G, seed=42)  
labels = nx.get_edge_attributes(G, 'weight')
nx.draw(G, pos, with_labels=True, node_size=700,
        node_color="lightblue", font_size=10, font_weight="bold")
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("Транспортна мережа обласних центрів України з вагами")
plt.show()
