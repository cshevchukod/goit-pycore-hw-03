#Завдання №2

import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    #Генерує відсортований список із quantity унікальних випадкових чисел.
    #Якщо параметри некоректні — повертає порожній список.

    # Перевірка коректності вхідних значень
    if min < 1 or max > 1000 or min > max or (max - min + 1) < quantity:
        return []

    # Генеруємо унікальні випадкові числа та сортуємо їх
    return sorted(random.sample(range(min, max + 1), quantity))

# Приклад виклику функції
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
