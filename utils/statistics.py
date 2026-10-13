# -*- coding: utf-8 -*-
"""Модуль статистических функций."""


def calculate_average(numbers):
    """Возвращает среднее арифметическое списка чисел."""
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)


def find_min(numbers):
    """Возвращает минимальное значение списка."""
    if not numbers:
        return None
    minimum = numbers[0]
    for num in numbers[1:]:
        if num < minimum:
            minimum = num
    return minimum


def find_max(numbers):
    """Возвращает максимальное значение списка."""
    if not numbers:
        return None
    maximum = numbers[0]
    for num in numbers[1:]:
        if num > maximum:
            maximum = num
    return maximum


def validate_numbers(numbers):
    """Проверяет, что список не пуст; иначе raises ValueError."""
    if not numbers:
        raise ValueError("Список измерений пуст")
