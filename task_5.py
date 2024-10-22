# Завдання 5. Візуалізація обходу бінарного дерева

# Використовуючи код із завдання 4 для побудови бінарного дерева, необхідно створити програму на Python, 
# яка візуалізує обходи дерева: у глибину та в ширину.
# Вона повинна відображати кожен крок у вузлах з різними кольорами, використовуючи 16-систему RGB (приклад #1296F0). 
# Кольори вузлів мають змінюватися від темних до світлих відтінків, залежно від послідовності обходу. 
# Кожен вузол при його відвідуванні має отримувати унікальний колір, який візуально відображає порядок обходу.

# Використовуйте стек та чергу, НЕ рекурсію.

import matplotlib.pyplot as plt
import networkx as nx
import uuid
import random
import time

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.color = '#000000'  # Початковий колір вузла (чорний)
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, update_colors):
    """Функція для візуалізації дерева з динамічним оновленням кольорів"""
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

    time.sleep(1)  # Затримка для кращої візуалізації


def bfs_visualize(root):
    """Обхід у ширину (BFS) з візуалізацією"""
    queue = [root]
    step = 0

    while queue:
        node = queue.pop(0)
        if node:
            # Генеруємо колір на основі порядку обходу (від темного до світлого)
            node.color = f"#{step:02x}{(150 + step * 8) % 256:02x}{(255 - step * 10) % 256:02x}"
            step += 1

            # Виводимо дерево на кожному кроці
            draw_tree(root, node)

            queue.append(node.left)
            queue.append(node.right)

def dfs_visualize(root):
    """Обхід у глибину (DFS) з візуалізацією"""
    stack = [root]
    step = 0

    while stack:
        node = stack.pop()
        if node:
            # Генеруємо колір на основі порядку обходу (від темного до світлого)
            node.color = f"#{step:02x}{(150 + step * 8) % 256:02x}{(255 - step * 10) % 256:02x}"
            step += 1

            # Виводимо дерево на кожному кроці
            draw_tree(root, node)

            # Спочатку додаємо правий вузол, щоб лівий оброблявся першим
            stack.append(node.right)
            stack.append(node.left)


# Створюємо дерево
root = Node(0)
root.left = Node(1)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)

# Візуалізація обходу в ширину (BFS)
print("Обхід у ширину (BFS):")
bfs_visualize(root)

# Візуалізація обходу в глибину (DFS)
print("Обхід у глибину (DFS):")
dfs_visualize(root)




