#sum_two_numbers

def sum_two_numbers(a, b):
    return a + b

#arithmetic_mean

def arithmetic_mean(numbers):
    if not numbers:
        raise ValueError("List cannot be empty")

    return sum(numbers) / len(numbers)

#reverse_string

def reverse_string(text):
    return text[::-1]

#longest_word

def longest_word(words):
    return max(words, key=len)

#find_substring

def find_substring(str1, str2):
    return str1.find(str2)