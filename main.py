# -*- coding: utf-8 -*-
"""Точка входа проекта «Измерения»."""

import json
import logging
from pathlib import Path

from utils.statistics import calculate_average, find_min, find_max, validate_numbers
from utils.reader import read_numbers


base_dir = Path(__file__).resolve().parent
config_path = base_dir / "config.json"
with open(config_path, "r", encoding="utf-8") as f:
    config = json.load(f)

logs_dir = base_dir / Path(config["log_file"]).parent
logs_dir.mkdir(exist_ok=True)
log_path = base_dir / config["log_file"]

logging.basicConfig(
    filename=str(log_path),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8",
)


def main():
    """Чтение измерений из файла и демонстрация статистических функций."""
    logging.info("Запуск программы")

    print(f"Параметры из {config_path}:")
    print(f"  input_file: {config['input_file']}")
    print(f"  log_file: {config['log_file']}")

    input_path = base_dir / config["input_file"]

    print(f"Текущий рабочий каталог: {Path.cwd()}")
    print(f"Путь к файлу данных: {input_path}")
    print(f"Файл существует: {input_path.exists()}")

    logs_dir = base_dir / "logs"
    logs_dir.mkdir(exist_ok=True)
    print(f"Каталог logs: {logs_dir} (существует)")

    try:
        numbers = read_numbers(str(input_path))
        logging.info("Файл успешно прочитан, значений: %d", len(numbers))
        validate_numbers(numbers)
    except FileNotFoundError:
        logging.error("Файл не найден: %s", input_path)
        print(f"Ошибка: файл не найден — {input_path}")
        return
    except ValueError as e:
        logging.error("Некорректное значение: %s", e)
        if "пуст" in str(e):
            print(f"Ошибка: {e}")
        else:
            print(f"Ошибка: некорректное значение в файле — {input_path}")
        return

    print(f"Список ({len(numbers)} значений): {numbers}")
    print(f"Среднее: {calculate_average(numbers):.2f}")
    print(f"Минимум: {find_min(numbers):.2f}")
    print(f"Максимум: {find_max(numbers):.2f}")

    logging.info("Программа завершена успешно")


if __name__ == "__main__":
    main()
