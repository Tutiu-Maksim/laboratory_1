# -*- coding: utf-8 -*-
"""Модуль чтения числовых данных из файла."""


def read_numbers(file_path):
    """Открывает файл, читает строки, преобразует в float и возвращает список."""
    numbers = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            stripped = line.strip()
            if stripped:
                numbers.append(float(stripped))
    return numbers
