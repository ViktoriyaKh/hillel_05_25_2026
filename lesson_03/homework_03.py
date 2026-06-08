# alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don't much care where ——" said Alice.\n"Then it doesn't matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you're sure to do that," said the Cat, "if you only walk long enough."'
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії

alice_in_wonderland = (
    '\'"Would you tell me, please, which way I ought to go from here?"\n'
    '"That depends a good deal on where you want to get to," said the Cat.\n'
    '"I don\'t much care where ——" said Alice.\n'
    '"Then it doesn\'t matter which way you go," said the Cat.\n"'
    '—— so long as I get somewhere," Alice added as an explanation.\n'
    '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'
)

print(alice_in_wonderland)

# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті

for char in alice_in_wonderland:
    if char == "'":
        print(char)

# task 03 == Виведіть змінну alice_in_wonderland на друк

print(alice_in_wonderland)


"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""

black_sea_area = 436402
azov_sea_area = 37800

total_area = black_sea_area + azov_sea_area

print(total_area)
print("Площа Чорного моря —", black_sea_area, "км².")
print("Площа Азовського моря —", azov_sea_area, "км².")
print("Разом Чорне та Азовське моря займають", total_area, "км².")

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""

total_goods = 375291
first_and_second = 250449
second_and_third = 222950

first_warehouse = (total_goods - second_and_third)
third_warehouse = (total_goods - first_and_second)
second_warehouse = (total_goods - (third_warehouse + first_warehouse))

print(first_warehouse)
print(second_warehouse)
print(third_warehouse)
print("На першому складі:", first_warehouse, "товарів.")
print("На другому складі:", second_warehouse, "товарів.")
print("На третьому складі:", third_warehouse, "товарів.")

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""

month = 18
payment_per_month = 1179
total_cost = payment_per_month * month

print(total_cost)
print("Комп’ютер оплачують 18 місяців по 1179 грн.")
print("Вартість комп’ютера становить", total_cost, "грн.")

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""

a = 8019%8
b = 9907%9
c = 2789%5
d = 7248%6
e = 7128%5
f = 19224%9

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print("a) Остача від ділення 8019 на 8 =", 8019 % 8)
print("b) Остача від ділення 9907 на 9 =", 9907 % 9)
print("c) Остача від ділення 2789 на 5 =", 2789 % 5)
print("d) Остача від ділення 7248 на 6 =", 7248 % 6)
print("e) Остача від ділення 7128 на 5 =", 7128 % 5)
print("f) Остача від ділення 19224 на 9 =", 19224 % 9)

# task 08
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

pizza_big_qty = 4
pizza_big_price = 274

pizza_middle_qty = 2
pizza_middle_price = 218

juice_qty = 4
juice_price = 35

cake_qty = 1
cake_price = 350

water_qty = 3
water_price = 21

total_cost = (
        pizza_big_qty * pizza_big_price +
        pizza_middle_qty * pizza_middle_price +
        juice_qty * juice_price +
        cake_qty * cake_price +
        water_qty * water_price
)

print(total_cost)
final_string = f"Для замовлення на день народження знадобиться {total_cost} грн."
print(final_string)

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""

photos = 232
photos_per_page = 8

pages = photos // photos_per_page
remainder = photos % photos_per_page

if remainder > 0:
    pages = pages + 1

print(pages)
final_string = f"Щоб вклеїти всі фото Ігорю знадобиться {pages} сторінок."
print(final_string)

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

distance = 1600
tank_capacity = 48
fuel_per_100km = 9

fuel_required = distance * fuel_per_100km // 100

refuels = fuel_required // tank_capacity
remainder = fuel_required % tank_capacity

if remainder > 0:
    refuels = refuels + 1

print(fuel_required)
print(refuels)
final_string = f"Для подорожі потрібно {fuel_required} літрів бензину."
print(final_string)
final_string = f"Мінімально потрібно заїхати на заправку {refuels} рази."
print(final_string)

