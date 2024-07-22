from collections import deque, defaultdict

cities = [
    "Київ", "Харків", "Дніпро", "Одеса", "Запоріжжя", "Львів", "Кривий Ріг",
    "Миколаїв", "Вінниця", "Херсон", "Полтава", "Чернігів",
    "Черкаси", "Хмельницький", "Чернівці", "Житомир", "Суми", "Рівне",
    "Івано-Франківськ", "Тернопіль", "Луцьк", "Ужгород", "Донецьк", "Луганськ", "Сімферополь"
]

roads = [
    ("Київ", "Харків"), ("Київ", "Житомир"), ("Київ",
                                              "Дніпро"), ("Київ", "Одеса"), ("Київ", "Львів"),
    ("Київ", "Вінниця"), ("Київ", "Чернігів"), ("Київ",
                                                "Черкаси"), ("Харків", "Дніпро"),
    ("Дніпро", "Запоріжжя"), ("Дніпро", "Одеса"), ("Дніпро", "Кривий Ріг"),
    ("Одеса", "Миколаїв"), ("Запоріжжя", "Донецьк"), ("Львів", "Хмельницький"),
    ("Львів", "Чернівці"), ("Львів",
                            "Тернопіль"), ("Львів", "Луцьк"), ("Львів", "Ужгород"),
    ("Вінниця", "Хмельницький"), ("Вінниця", "Житомир"), ("Херсон", "Миколаїв"),
    ("Херсон", "Запоріжжя"), ("Полтава", "Харків"), ("Полтава", "Дніпро"),
    ("Чернігів", "Суми"), ("Черкаси", "Кіровоград"), ("Черкаси", "Полтава"),
    ("Чернівці", "Івано-Франківськ"), ("Житомир", "Рівне"), ("Суми", "Харків"),
    ("Рівне", "Луцьк"), ("Івано-Франківськ",
                         "Тернопіль"), ("Донецьк", "Луганськ"), ("Сімферополь", "Херсон")
]

graph = defaultdict(list)
for city1, city2 in roads:
    graph[city1].append(city2)
    graph[city2].append(city1)


def bfs(start, goal):
    visited = set()
    queue = deque([(start, [start])])
    while queue:
        (vertex, path) = queue.popleft()
        for next in set(graph[vertex]) - visited:
            if next == goal:
                return path + [next]
            else:
                visited.add(next)
                queue.append((next, path + [next]))
    return None


def dfs(start, goal, path=None):
    if path is None:
        path = []
    path = path + [start]
    if start == goal:
        return path
    for node in set(graph[start]) - set(path):
        new_path = dfs(node, goal, path)
        if new_path:
            return new_path
    return None


start_city = "Київ"
goal_city = "Ужгород"

bfs_path = bfs(start_city, goal_city)
dfs_path = dfs(start_city, goal_city)

print(f"BFS path from {start_city} to {goal_city}: {bfs_path}")
print(f"DFS path from {start_city} to {goal_city}: {dfs_path}")

if bfs_path:
    print(f"BFS finds a path: {bfs_path}")
else:
    print("BFS did not find a path.")

if dfs_path:
    print(f"DFS finds a path: {dfs_path}")
else:
    print("DFS did not find a path.")
