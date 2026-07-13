import pytest

from homeworks import sum_two_numbers, arithmetic_mean, reverse_string, longest_word, find_substring
def test_sum_two_numbers_positive():
    assert sum_two_numbers(2, 3) == 5

def test_sum_two_numbers_zero():
    assert sum_two_numbers(0, 0) == 0

def test_sum_two_numbers_negative():
    assert sum_two_numbers(-5, 10) == 5


def test_arithmetic_mean_several_numbers():
    assert arithmetic_mean([2, 4, 6, 8]) == 5

def test_arithmetic_mean_negative_numbers():
    assert arithmetic_mean([-2, -4, -6]) == -4

def test_arithmetic_mean_empty_list():
    with pytest.raises(ValueError):
        arithmetic_mean([])


def test_reverse_string_word():
    assert reverse_string("hello") == "olleh"

def test_reverse_string_sentence():
    assert reverse_string("Hello World") == "dlroW olleH"

def test_reverse_string_numbers():
    assert reverse_string("12345") == "54321"


def test_longest_word_list():
    assert longest_word(["cat", "elephant", "dog"]) == "elephant"

def test_longest_word_sentence():
    sentence = "I struggle with Python programming"
    assert longest_word(sentence.split()) == "programming"


def test_find_substring_found():
    assert find_substring("Hello world", "world") == 6

def test_find_substring_not_found():
    assert find_substring("Hello world", "Python") == -1

def test_find_substring_at_start():
    assert find_substring("Python is hard for me", "Python") == 0