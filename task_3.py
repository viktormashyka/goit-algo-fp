# Завдання 3. Дерева, алгоритм Дейкстри

# Розробіть алгоритм Дейкстри для знаходження найкоротших шляхів у зваженому графі, використовуючи бінарну купу. 
# Завдання включає створення графа, використання піраміди для оптимізації вибору вершин та обчислення 
# найкоротших шляхів від початкової вершини до всіх інших.

import heapq

def dijkstra(graph, start):
    # Ініціалізуємо відстані до всіх вершин як нескінченні, крім початкової вершини
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    
    # Створюємо мін-купу (бінарну купу)
    priority_queue = [(0, start)]  # (відстань, вершина)

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Якщо відстань до поточної вершини більша за ту, що ми вже знаємо, пропускаємо її
        if current_distance > distances[current_vertex]:
            continue

        # Оновлюємо відстань для кожного сусіда
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Якщо знайдено коротший шлях до сусіда
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Приклад графа
graph = {
    'A': {'B': 5, 'C': 2},
    'B': {'A': 5, 'C': 4, 'D': 1},
    'C': {'A': 2, 'B': 4, 'D': 7},
    'D': {'B': 1, 'C': 7}
}

# Визначення найкоротших шляхів від вершини 'A'
distances = dijkstra(graph, 'A')
print(distances) # {'A': 0, 'B': 5, 'C': 2, 'D': 6}
