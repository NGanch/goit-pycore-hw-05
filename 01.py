def caching_fibonacci():
    # Створення словника для кешування
    cache = {}

    # Внутрішня функція для обчислення чисел Фібоначчі
    def fibonacci(n):
        # Базові випадки
        if n <= 0:
            return 0
        if n == 1:
            return 1

        # Перевірка наявності у кеші
        if n in cache:
            return cache[n]

        # Обчислення та збереження у кеші
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    # Повернення внутрішньої функції
    return fibonacci

# Приклад використання
if __name__ == "__main__":
    # Отримуємо функцію fibonacci
    fib = caching_fibonacci()

    # Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
    print(fib(10))  # Виведе 55
    print(fib(15))  # Виведе 610