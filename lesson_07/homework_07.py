# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""

# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15

def multiplication_table(number):
    multiplier = 1

    while True:
        result = number * multiplier

        if result > 25:
            break

        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        multiplier += 1

multiplication_table(3)

# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""

def sum_two_numbers(a, b):
    return a + b

print(sum_two_numbers(10, 12))

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""

def arithmetic_mean(numbers):
    return sum(numbers) / len(numbers)

nums = [2, 3, 4, 5, 6, 8, 9]
print(arithmetic_mean(nums))

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""

def reverse_string(text):
    return text[::-1]

print(reverse_string("Hello World"))

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""

def longest_word(words):
    return max(words, key=len)

print(longest_word(["cat", "dog", "friend", "umbrella"]))

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""

# def find_substring(str1, str2):
#
#     return -1
#
# str1 = "Hello, world!"
# str2 = "world"
# print(find_substring(str1, str2)) # поверне 7
#
# str1 = "The quick brown fox jumps over the lazy dog"
# str2 = "cat"
# print(find_substring(str1, str2)) # поверне -1

def find_substring(str1, str2):
    return str1.find(str2)

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2))

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2))

"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""

# task 7

"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""

def calculate_sea_areas(black_sea_area, azov_sea_area):
    """
    Обчислюємо загальну площу Чорного та Азовського морів.

    Parameters:
    black_sea_area (float or int): площа Чорного моря в км2
    azov_sea_area (float or int): площа Азовського моря в км2

    Returns:
    float: загальна площа двох морів у км2
    """
    total_area = black_sea_area + azov_sea_area
    return total_area

black_sea = 436402
azov_sea = 37800

result = calculate_sea_areas(black_sea, azov_sea)
print(result)

# task 8

"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""

def calculate_warehouses(total, first_second, second_third):
    """
    Обчислюємо кількість товарів на кожному з трьох складів.

    Parameters:
    total (int): загальна кількість товарів
    first_second (int): кількість товарів на 1 і 2 складах
    second_third (int): кількість товарів на 2 і 3 складах

    Returns:
    tuple: кількість товарів на 1, 2 і 3 складах
    """

    second = (first_second + second_third) - total
    first = first_second - second
    third = second_third - second

    return first, second, third

total = 375291
first_second = 250449
second_third = 222950

result = calculate_warehouses(total, first_second, second_third)
print(result)

# task 9

"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""

def calculate_total_cost():
    """
    Обчислюємо загальну вартість замовлення для дня народження.
    """

    pizza_large = 4 * 274
    pizza_medium = 2 * 218
    juice = 4 * 35
    cake = 1 * 350
    water = 3 * 21

    total_cost = pizza_large + pizza_medium + juice + cake + water

    return total_cost

result = calculate_total_cost()
print(result)

# task 10

"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""

def car_trip_fuel(distance_km, consumption_per_100km, tank_capacity):
    """
    Обчислюємо:
    1) загальну кількість бензину для поїздки
    2) мінімальну кількість заправок (повний бак)

    Parameters:
    distance_km (float): відстань поїздки в км
    consumption_per_100km (float): витрата пального на 100 км
    tank_capacity (float): місткість бака в літрах

    Returns:
    tuple: (загальна витрата пального, кількість заправок)
    """

    fuel_needed = (distance_km / 100) * consumption_per_100km

    full_tanks_needed = fuel_needed / tank_capacity

    refuels = int(full_tanks_needed) if full_tanks_needed.is_integer() else int(full_tanks_needed) + 1

    return fuel_needed, refuels

distance = 1600
consumption = 9
tank = 48

result = car_trip_fuel(distance, consumption, tank)
print(result)
