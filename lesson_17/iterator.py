class ReverseIterator:
    def __init__(self, data):
        self.data = data
        self.index = len(data) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration

        item = self.data[self.index]
        self.index -= 1
        return item

numbers = [10, 20, 30, 40, 50]

for num in ReverseIterator(numbers):
    print(num)
print("=" * 30)

class EvenIterator:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.n:
            raise StopIteration

        number = self.current
        self.current += 2
        return number

N = 40

for num in EvenIterator(N):
    print(num)
