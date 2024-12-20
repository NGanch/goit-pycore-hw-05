import re
from typing import Callable

def generator_numbers(text: str):
    """
    Аналізує текст і генерує всі дійсні числа, які чітко відокремлені пробілами.

    :param text: Вхідний текст
    :return: Генератор чисел
    """
    pattern = r'\b\d+\.\d+|\b\d+\b'  # Регулярний вираз для пошуку цілих та дійсних чисел
    for match in re.finditer(pattern, text):
        yield float(match.group())

def sum_profit(text: str, func: Callable):
    """
    Використовує генератор для підсумовування чисел у тексті.

    :param text: Вхідний текст
    :param func: Функція-генератор чисел
    :return: Загальний дохід
    """
    return sum(func(text))

if __name__ == "__main__":
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")