def even_numbers(n):
    for number in range(0, n + 1, 2):
        yield number

N = 40

for num in even_numbers(N):
    print(num)
print("=" * 30)

def fibonacci(n):
    a = 0
    b = 1

    while a <= n:
        yield a
        a, b = b, a + b

N = 40

for num in fibonacci(N):
    print(num)