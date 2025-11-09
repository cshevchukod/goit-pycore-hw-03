
from datetime import datetime # модуль для роботи

def get_days_from_today(date_str: str) -> int:
    #Обчислює кількість днів між заданою датою і сьогоднішньою.
    #Формат вхідної дати: 'РРРР-ММ-ДД'.

    try:
        # Перетворюємо рядок у об’єкт дати
        user_date = datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        # Обробка некоректного формату дати
        print("Невірний формат дати. Використовуйте 'РРРР-ММ-ДД'.")
        return None

    # Поточна дата
    today_date = datetime.today()

    # Різниця між поточною та заданою датами у днях
    return today_date.toordinal() - user_date.toordinal()

print(get_days_from_today("2025-01-01"))

print('')

import random  # модуль для роботи

def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    #Генерує відсортований список із quantity унікальних випадкових чисел.
    #Якщо параметри некоректні — повертає порожній список.

    # Перевірка коректності вхідних значень
    if min < 1 or max > 1000 or min > max or (max - min + 1) < quantity:
        return []  # повертаємо пустий список, якщо умови не виконані

    # Генеруємо унікальні випадкові числа та сортуємо їх
    return sorted(random.sample(range(min, max + 1), quantity))

# Приклад виклику функції
print(get_numbers_ticket(1, 1000, 6))


