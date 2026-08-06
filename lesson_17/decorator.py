def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Arguments: args={args}, kwargs={kwargs}")

        result = func(*args, **kwargs)

        print(f"Result: {result}")
        return result

    return wrapper

@logger
def add(a, b):
    return a + b

print(add(5, 3))
print("="*30)


def exception_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as error:
            print(f"Error: {error}")

    return wrapper

@exception_handler
def divide(a, b):
    return a / b

print(divide(10, 2))
print(divide(10, 0))

