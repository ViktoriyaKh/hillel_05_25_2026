random_string = input("строка:")

unique_chars = set()

for char in random_string:
    unique_chars.add(char)

if len(unique_chars) > 10:
    print(True)
else:
    print(False)
