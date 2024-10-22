# Завдання 1. Структури даних. Сортування. Робота з однозв'язним списком

# Для реалізації однозв'язного списку (приклад реалізації можна взяти з конспекту) необхідно:
# написати функцію, яка реалізує реверсування однозв'язного списку, змінюючи посилання між вузлами;
# розробити алгоритм сортування для однозв'язного списку, наприклад, сортування вставками або злиттям;
# написати функцію, що об'єднує два відсортовані однозв'язні списки в один відсортований список.

# Реверсування однозв'язного списку
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Додавання елемента в кінець списку
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # Функція для реверсування списку
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    # Виведення списку
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Сортування однозв'язного списку методом злиття
# Допоміжна функція для знаходження середини списку
def get_middle(head):
    if not head:
        return head

    slow = head
    fast = head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

# Сортування методом злиття
def merge_sort(head):
    if not head or not head.next:
        return head

    middle = get_middle(head)
    next_to_middle = middle.next
    middle.next = None

    left = merge_sort(head)
    right = merge_sort(next_to_middle)

    return sorted_merge(left, right)

# Функція для злиття двох відсортованих списків
def sorted_merge(left, right):
    if not left:
        return right
    if not right:
        return left

    if left.data <= right.data:
        result = left
        result.next = sorted_merge(left.next, right)
    else:
        result = right
        result.next = sorted_merge(left, right.next)

    return result

# Об'єднання двох відсортованих однозв'язних списків
def merge_sorted_lists(list1, list2):
    if not list1:
        return list2
    if not list2:
        return list1

    if list1.data <= list2.data:
        result = list1
        result.next = merge_sorted_lists(list1.next, list2)
    else:
        result = list2
        result.next = merge_sorted_lists(list1, list2.next)

    return result


# Приклад використання
# Створюємо два списки
list1 = LinkedList()
list1.append(1)
list1.append(3)
list1.append(5)

list2 = LinkedList()
list2.append(2)
list2.append(4)
list2.append(6)

# Об'єднуємо відсортовані списки
merged_list_head = merge_sorted_lists(list1.head, list2.head)
merged_list = LinkedList()
merged_list.head = merged_list_head
merged_list.print_list()

# Реверсування списку
merged_list.reverse()
merged_list.print_list()

# Сортування методом злиття
sorted_head = merge_sort(merged_list.head)
sorted_list = LinkedList()
sorted_list.head = sorted_head
sorted_list.print_list()
