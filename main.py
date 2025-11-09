#Завдання №1

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

# Приклад виклику функції
print(get_days_from_today("2025-01-01"))
print(get_days_from_today("2026-10-09"))

print('')

#Завдання №2

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
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)

print('')

#Завдання №3

import re # модуль для роботи

def normalize_phone(phone_number: str) -> str:
    # залишаємо тільки цифри і '+'
    clean_number = re.sub(r"[^+\d]", "", phone_number)

    # якщо номер не починається з '+'
    if not re.match(r"^\+", clean_number):
        # якщо починається з 380 — додаємо '+'
        if re.match(r"^380", clean_number):
            clean_number = "+" + clean_number
        # інакше додаємо '+38'
        else:
            clean_number = "+38" + clean_number

    return clean_number

# Приклад виклику функції
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]
sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)

print('')

#Завдання №4

from datetime import datetime, timedelta # модуль для роботи

def get_upcoming_birthdays(users):
    result = []  # список для збереження користувачів, яких треба привітати
    today = datetime.today().date()  # поточна дата
    window_end = today + timedelta(days=7)  # межа для 7-денного періоду

    for user in users:  # проходимо по кожному користувачу у списку
        # перетворюємо дату народження з тексту у формат дати
        bday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        # визначаємо, коли святкувати цього року чи наступного
        if (bday.month, bday.day) >= (today.month, today.day):
            target_year = today.year
        else:
            target_year = today.year + 1

        # створюємо дату майбутнього дня народження у вибраному році
        mm = bday.strftime("%m")
        dd = bday.strftime("%d")

        # будуємо дату привітання; 29.02 → 28.02 у невисокосний рік
        try:
            bday_date = datetime.strptime(str(target_year) + "." + mm + "." + dd, "%Y.%m.%d").date()
        except ValueError:
            if mm == "02" and dd == "29":
                bday_date = datetime.strptime(str(target_year) + ".02.28", "%Y.%m.%d").date()
            else:
                continue  # некоректна дата в даних
        
        # якщо це вихідні (субота або неділя) — переносимо привітання на понеділок
        if bday_date.weekday() >= 5:  # 5=сб, 6=нд
            bday_date = bday_date + timedelta(days=7 - bday_date.weekday())

        # перевіряємо, чи день народження потрапляє у найближчі 7 днів
        if today <= bday_date <= window_end:
            result.append({
                "name": user["name"],
                "congratulation_date": bday_date.strftime("%Y.%m.%d")
            })

    return result  # повертаємо список привітань

# Приклад виклику функції
users = [
    {"name": "John Doe", "birthday": "1985.11.13"},
    {"name": "Jane Smith", "birthday": "1990.11.17"}
]
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)