"""Основные арифметические функции."""
def add(a: float, b: float) -> float:
    """Возвращает сумму двух чисел."""
    return a + b
def subtract(a: float, b: float) -> float:
    """Возвращает разность двух чисел."""
    return a - b
def multiply(a: float, b: float) -> float:
    """Возвращает произведение двух чисел."""
    return a * b
def divide(a: float, b: float) -> float:
    """Делит a на b.

    Выбрасывает ValueError при делении на ноль.
    """
    if b == 0:
        raise ValueError("Division by zero")
    return a / b
def power(a: float, b: float) -> float:
    """Возводит число a в степень b."""
    return a ** b
