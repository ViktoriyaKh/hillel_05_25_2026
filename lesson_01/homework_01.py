# task 01
"""
Виправте синтаксичні помилки
print("Hello", end = " ")
    print("world!")
"""
print("Hello", end=" ")
print("world!")

# task 02
"""
Виправте синтаксичні помилки
hello = "Hello"
world = "world"
if True:
print(f"{hello} {world}!")
"""
hello = "Hello"
world = "world"
if True:
    print(f"{hello} {world}!")

# task 03
"""
Вcтавте пропущену змінну у ф-цію print
for letter in "Hello world!":
    print()
"""
for letter in "Hello world!":
    print(letter)

# task 04
"""
Зробіть так, щоб кількість бананів була
завжди в чотири рази більша, ніж яблук
apples = 2
banana = x
"""
apples = 2
banana = apples * 4
print(banana)

# task 05
"""
Виправте назви змінних
1_storona = 1
?torona_2 = 2
сторона_3 = 3
$torona_4 = 4
"""
storona_1 = 1
storona_2 = 2
storona_3 = 3
storona_4 = 4

# task 06
"""
Порахуйте периметр фігури з task 05
та виведіть його для користувача
perimetery = ? + ? + ? + ?
print()
"""
storona_1 = 1
storona_2 = 2
storona_3 = 3
storona_4 = 4

perimetery = storona_1 + storona_2 + storona_3 + storona_4
print(perimetery)

"""
    # Задачі 07 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""

# task 07
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""
planted_apple = 4
planted_pear = planted_apple + 5
planted_plum = planted_apple - 2

all_trees = (planted_apple, planted_pear, planted_plum)
all_trees_quantity = sum(all_trees)

print(all_trees_quantity)

#результат:15

# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""
air_temperature = 5 + 0
afternoon_temperature = air_temperature - 10
evening_temperature = afternoon_temperature + 4

print(evening_temperature)

#результат:-1

# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""
all_boys = 24
all_girls = 24 / 2
today_boys = all_boys - 1
today_girls = all_girls - 2

all_children_today = (today_boys, today_girls)
all_children = sum(all_children_today)

print(all_children)

#результат:33

# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
first_book_cost = 8
second_book_cost = first_book_cost + 2
third_book_cost = (first_book_cost + second_book_cost) / 2

all_books = (first_book_cost, second_book_cost, third_book_cost)
all_books_cost = sum(all_books)

print(all_books_cost)

#результат:27

