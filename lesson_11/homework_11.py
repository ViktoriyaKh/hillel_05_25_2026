data = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]

def sum_numbers(line):
    try:
        numbers = line.split(",")
        total = 0
        for num in numbers:
            total += int(num)
        return total
    except ValueError:
        return "Не можу це зробити!"

for item in data:
    print(sum_numbers(item))