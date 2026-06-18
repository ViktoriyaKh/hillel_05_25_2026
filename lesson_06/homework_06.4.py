lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sum_even = 0

for num in lst:
    if num % 2 == 0:
        sum_even += num

print(sum_even)