import datetime  # Импортирует модуль datetime для работы с датами

def get_weekday(day, month, year): # Создаёт объект даты 
    try:
        date_obj = datetime.date(year, month, day)
        weekdays = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
        return weekdays[date_obj.weekday()]  # Получает индекс дня недели (0-6) и возвращаем соответствующее название
    except ValueError: # Если дата некорректна (например, 31 февраля), возвращает None
        return None
    
#is_leap_year Функция определяет, является ли переданный
# год високосным по григорианскому календарю. Возвращает True или False в зависимости от результата проверки.
#(год кратен 4 И год не кратен 100) ИЛИ (год кратен 400)
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

#Функция вычисляет возраст человека в годах на основе его даты рождения и текущей даты. 
#Возвращает полное количество лет (целое число) или None при некорректной дате рождения.
def calculate_age(day, month, year):
    today = datetime.date.today() # Получает текущую дату
    try:
        birth_date = datetime.date(year, month, day) # Создаёт дату рождения
    except ValueError:
        return None  # Если дата невалидна
    age = today.year - birth_date.year # Вычисляем возраст
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1  # Если день рождения ещё не наступил
    return age

def print_digit_star(digit):  # Словарь с шаблонами для каждого символа
    patterns = {
        '0': ["***", "* *", "* *", "* *", "***"],
        '1': ["  *", "  *", "  *", "  *", "  *"],
        '2': ["***", "  *", "***", "*  ", "***"],
        '3': ["***", "  *", "***", "  *", "***"],
        '4': ["* *", "* *", "***", "  *", "  *"],
        '5': ["***", "*  ", "***", "  *", "***"],
        '6': ["***", "*  ", "***", "* *", "***"],
        '7': ["***", "  *", "  *", "  *", "  *"],
        '8': ["***", "* *", "***", "* *", "***"],
        '9': ["***", "* *", "***", "  *", "***"],
        '.': ["   ", "   ", "   ", "  *", "   "]
    }     # Точка в нижней позиции
    return patterns.get(digit, ["   ", "   ", "   ", "   ", "   "])  
# Возвращает шаблон или пустой шаблон для неизвестных символов

#Функция ничего не возвращает, только выводит на экран
def print_date_star(day, month, year):
    date_str = f"{day:02d}.{month:02d}.{year:4d}"     # Форматирует дату: день (2 цифры) + точка + месяц (2 цифры) + точка + год (4 цифры)
    patterns = [print_digit_star(char) for char in date_str]     # Для каждого символа в строке получает его звёздный шаблон
    for row in range(5):       # Проходит по 5 строк (каждый символ имеет высоту 5)
        line_parts = []          # Для каждого шаблона берёт строку с текущим индексом row
        for pat in patterns:
            line_parts.append(pat[row])
        print("  ".join(line_parts))             # Склеивает все части через 2 пробела и выводит


def main():

    # Вывод заголовка
    print("=" * 50)
    print("        КАЛЬКУЛЯТОР ДНЯ РОЖДЕНИЯ")
    print("=" * 50)
    
    # Ввод даты с проверкой
    while True:
        try:
            day = int(input("День (1-31): "))
            month = int(input("Месяц (1-12): "))
            year = int(input("Год (например, 1990): "))
            datetime.date(year, month, day) # Проверка существования даты
            break
        except ValueError:
            print("Ошибка! Некорректная дата.\n")
    # Определение дня недели
    weekday = get_weekday(day, month, year)
    if weekday:
        print(f"\nДень недели: {weekday}")
    else:
        print("\nОшибка: неверная дата!")
        return
    
    # Проверка високосности
    if is_leap_year(year):
        print("Год был високосным (366 дней)")
    else:
        print("Год был невисокосным (365 дней)")
    
    # Расчёт возраста
    age = calculate_age(day, month, year)
    if age is not None:
        print(f"Ваш возраст: {age} лет")
    
    # Вывод ASCII-арта
    print("\n" + "=" * 50)
    print("        ДАТА РОЖДЕНИЯ НА ТАБЛО")
    print("=" * 50)
    print_date_star(day, month, year)

if __name__ == "__main__":
    main()
