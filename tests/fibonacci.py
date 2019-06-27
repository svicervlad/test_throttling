"""
для тестирования работы процессора на одном ядре не продолжительное врямя
рекомендуемое n = 42
"""


def fibonacci(num):
    """
    вычисляет чило фибоначи
    """
    if num in {1, 2}:
        return 1
    return fibonacci(num - 1) + fibonacci(num - 2)
