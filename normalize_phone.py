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