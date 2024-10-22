# Завдання 6. Жадібні алгоритми та динамічне програмування

# Необхідно написати програму на Python, яка використовує два підходи — жадібний алгоритм та алгоритм динамічного 
# програмування для розв’язання задачі вибору їжі з найбільшою сумарною калорійністю в межах обмеженого бюджету.
# Кожен вид їжі має вказану вартість і калорійність. Дані про їжу представлені у вигляді словника, 
# де ключ — назва страви, а значення — це словник з вартістю та калорійністю.

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

# Розробіть функцію greedy_algorithm жадібного алгоритму, яка вибирає страви, максимізуючи співвідношення калорій 
# до вартості, не перевищуючи заданий бюджет.

# Для реалізації алгоритму динамічного програмування створіть функцію dynamic_programming, яка обчислює 
# оптимальний набір страв для максимізації калорійності при заданому бюджеті.

def greedy_algorithm(items, budget):
    # Обчислюємо співвідношення калорій до вартості для кожної страви
    items_sorted = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    
    total_calories = 0
    total_cost = 0
    chosen_items = []

    for item, info in items_sorted:
        if total_cost + info['cost'] <= budget:
            chosen_items.append(item)
            total_calories += info['calories']
            total_cost += info['cost']
    
    return chosen_items, total_calories, total_cost

# Приклад використання
budget = 100
chosen_items, total_calories, total_cost = greedy_algorithm(items, budget)
print(f"Обрані страви (жадібний алгоритм): {chosen_items}")
print(f"Загальна калорійність: {total_calories}")
print(f"Загальна вартість: {total_cost}")


def dynamic_programming(items, budget):
    # Створюємо таблицю для збереження максимальної калорійності для кожного бюджету
    dp = [0] * (budget + 1)
    chosen_items = [[] for _ in range(budget + 1)]
    
    for item, info in items.items():
        cost = info['cost']
        calories = info['calories']
        
        # Оновлюємо таблицю для поточного елемента
        for b in range(budget, cost - 1, -1):
            if dp[b - cost] + calories > dp[b]:
                dp[b] = dp[b - cost] + calories
                chosen_items[b] = chosen_items[b - cost] + [item]

    return chosen_items[budget], dp[budget]

# Приклад використання
chosen_items_dp, total_calories_dp = dynamic_programming(items, budget)
print(f"Обрані страви (динамічне програмування): {chosen_items_dp}")
print(f"Загальна калорійність: {total_calories_dp}")
