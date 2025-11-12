#Завдання №1

from datetime import datetime

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

# Приклад виклику функції
print(get_days_from_today("2025-01-01"))
print(get_days_from_today("2026-10-09"))