# Завдання 7. Використання методу Монте-Карло

# Необхідно написати програму на Python, яка імітує велику кількість кидків кубиків, обчислює суми чисел, 
# які випадають на кубиках, і визначає ймовірність кожної можливої суми.
# Створіть симуляцію, де два кубики кидаються велику кількість разів. Для кожного кидка визначте суму чисел, 
# які випали на обох кубиках. Підрахуйте, скільки разів кожна можлива сума (від 2 до 12) з’являється у процесі 
# симуляції. Використовуючи ці дані, обчисліть імовірність кожної суми.
# На основі проведених імітацій створіть таблицю або графік, який відображає ймовірності кожної суми, виявлені 
# за допомогою методу Монте-Карло.
# Таблиця ймовірностей сум при киданні двох кубиків виглядає наступним чином.

# Порівняйте отримані за допомогою методу Монте-Карло результати з аналітичними розрахунками, наведеними в таблиці вище.

import random
import matplotlib.pyplot as plt
import numpy as np

# Функція для симуляції кидків кубиків
def simulate_dice_rolls(num_rolls):
    results = {i: 0 for i in range(2, 13)}  # Всі можливі суми від 2 до 12
    
    for _ in range(num_rolls):
        dice1 = random.randint(1, 6)  # Перший кубик
        dice2 = random.randint(1, 6)  # Другий кубик
        dice_sum = dice1 + dice2
        results[dice_sum] += 1  # Збільшуємо лічильник для поточної суми

    return results

# Функція для обчислення ймовірностей
def calculate_probabilities(results, num_rolls):
    probabilities = {sum_value: count / num_rolls for sum_value, count in results.items()}
    return probabilities

# Функція для побудови графіка
def plot_probabilities(probabilities):
    sums = list(probabilities.keys())
    probs = list(probabilities.values())
    
    plt.bar(sums, probs, color='skyblue', edgecolor='black')
    plt.xlabel("Сума на двох кубиках")
    plt.ylabel("Ймовірність")
    plt.title("Ймовірність сум при киданні двох кубиків (Метод Монте-Карло)")
    plt.xticks(sums)
    plt.show()

# Симуляція
num_rolls = 100000  # Кількість симуляцій
results = simulate_dice_rolls(num_rolls)
probabilities = calculate_probabilities(results, num_rolls)

# Виведення результатів
for sum_value, probability in probabilities.items():
    print(f"Сума {sum_value}: ймовірність {probability:.4f}")

# Побудова графіка
plot_probabilities(probabilities)

# Аналітичні ймовірності для порівняння
analytical_probabilities = {
    2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36, 6: 5/36, 7: 6/36,
    8: 5/36, 9: 4/36, 10: 3/36, 11: 2/36, 12: 1/36
}

# Побудова графіка для порівняння аналітичних ймовірностей
def plot_analytical_probabilities(analytical_probabilities):
    sums = list(analytical_probabilities.keys())
    probs = list(analytical_probabilities.values())
    
    plt.bar(sums, probs, color='orange', edgecolor='black')
    plt.xlabel("Сума на двох кубиках")
    plt.ylabel("Ймовірність")
    plt.title("Аналітичні ймовірності сум при киданні двох кубиків")
    plt.xticks(sums)
    plt.show()

plot_analytical_probabilities(analytical_probabilities)

# Порівняння результатів
# Метод Монте-Карло: Отримані ймовірності будуть близькими до аналітичних, але можуть мати незначні відхилення 
# залежно від кількості симуляцій.
# Аналітичні ймовірності: Вони визначені точно на основі кількості можливих комбінацій для кожної суми.

# Висновки:
# Метод Монте-Карло дозволяє наближено визначити ймовірності для випадкових подій. При великій кількості 
# симуляцій отримані значення будуть дуже близькими до аналітичних результатів. Це підтверджує ефективність 
# цього методу для вирішення задач, пов'язаних із ймовірністю випадкових подій.