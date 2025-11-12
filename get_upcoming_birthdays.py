#Завдання №4

from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    result = [] 
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

        # будуємо дату привітання
        try:
            bday_date = datetime.strptime(str(target_year) + "." + mm + "." + dd, "%Y.%m.%d").date()
        except ValueError:
            #29.02 → 28.02 у невисокосний рік
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

    return result

# Приклад виклику функції
users = [
    {"name": "John Doe", "birthday": "1985.11.13"},
    {"name": "Jane Smith", "birthday": "1990.11.17"}
]
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)