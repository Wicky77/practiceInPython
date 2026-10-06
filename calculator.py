import numpy as np

def add(a, b):
    """Складывает два числа и возвращает результат."""
    return a + b

def subtract(a, b):
    """Вычитает второе число из первого."""
    return a - b

def multiply(a, b):
    """Умножает два числа."""
    return a * b

def divide(a, b):
    """Делит первое число на второе."""
    return a / b

# Тестовый скрипт
if __name__ == "__main__":
    print("Сложение: " + str(add(10, 5)))
    print("Вычитание: " + str(subtract(10, 5)))
    print("Умножение: " + str(multiply(10, 5)))
    print("Деление: " + str(divide(10, 5)))
    
    # Проверяем, что numpy работает
    arr = np.array([1, 2, 3, 4, 5])
    print("Среднее значение массива: " + str(np.mean(arr)))