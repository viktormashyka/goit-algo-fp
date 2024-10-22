# Завдання 4. Візуалізація піраміди

# Побудуйте функцію, що буде візуалізувати бінарну купу.

import networkx as nx
import matplotlib.pyplot as plt
import uuid

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Колір вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

def build_heap_tree(arr):
    """Функція для перетворення масиву на дерево (бінарну купу)"""
    if not arr:
        return None
    
    nodes = [Node(val) for val in arr]
    
    for i in range(len(arr)):
        left_index = 2 * i + 1
        right_index = 2 * i + 2
        
        if left_index < len(arr):
            nodes[i].left = nodes[left_index]
        if right_index < len(arr):
            nodes[i].right = nodes[right_index]
    
    return nodes[0]  # Повертаємо кореневий вузол

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    """Функція для додавання ребер у граф та визначення позицій вузлів"""
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Додаємо вузол
        if node.left:
            graph.add_edge(node.id, node.left.id)  # Додаємо ребро
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)  # Додаємо ребро
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root):
    """Функція для візуалізації дерева"""
    tree = nx.DiGraph()  # Створюємо направлений граф
    pos = {tree_root.id: (0, 0)}  # Початкова позиція кореня
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Мітки вузлів

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

# Створення бінарної купи з масиву
heap_array = [20, 15, 10, 8, 7, 9, 5, 3, 2]
heap_tree_root = build_heap_tree(heap_array)

# Відображення дерева
draw_tree(heap_tree_root)