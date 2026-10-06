import random

def task1():
    #Переводит температуру из Цельсия в Фаренгейты и Кельвины
    celsius = float(input("Введите температуру в градусах Цельсия: "))
    fahrenheit = celsius * 9 / 5 + 32
    kelvin = celsius + 273.15
    print("Температура в Фаренгейтах: " + str(round(fahrenheit, 2)))
    print("Температура в Кельвинах: " + str(round(kelvin, 2)))

def task2():
    """Проверяет число на чётность, знак и попадание в диапазон [10, 50]"""
    n = int(input("Введите целое число: "))
    
    if n % 2 == 0:
        print("Число чётное")
    else:
        print("Число нечётное")

    if n > 0:
        print("Число положительное")
    elif n < 0:
        print("Число отрицательное")
    else:
        print("Число равно нулю")

    if n >= 10 and n <= 50:
        print("Число принадлежит диапазону [10, 50]")
    else:
        print("Число не принадлежит диапазону [10, 50]")

def task3():
    """Генерирует пароль из 8 символов: 3 буквы, 3 цифры и 2 спецсимвола.
    Собирает пароль, случайно выбирая элементы из заданных строк"""
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    symbols = "!@#$%^&*"
    password = ""

    for i in range(3):
        password = password + letters[random.randint(0, len(letters) - 1)]

    for i in range(3):
        password = password + digits[random.randint(0, len(digits) - 1)]

    for i in range(2):
        password = password + symbols[random.randint(0, len(symbols) - 1)]

    print("Сгенерированный пароль: " + password)

def task4():
    """Считает частоту каждого символа в строке и находит 3 самых частых.
    Игнорирует регистр, использует словарь для подсчёта и простой перебор для поиска максимума"""
    text = input("Введите строку: ")
    text = text.lower()
    counts = {}
    
    for char in text:
        if char in counts:
            counts[char] = counts[char] + 1 #сдвигаем счётчик, чтобы подсчитать колво одинаковых символов
        else:
            counts[char] = 1

    print("Количество каждого символа:")
    for char in counts:
        print("  '" + char + "': " + str(counts[char]))

    top = []
    for i in range(3):
        max_char = ""
        max_count = 0
        for char in counts:
            if counts[char] > max_count and char not in top: #ищем 3 самых частых символа по очереди без повтора
                max_count = counts[char]
                max_char = char
        if max_char != "":
            top.append(max_char)
            print(str(i + 1) + ". '" + max_char + "' — " + str(max_count) + " раз(а)")

def task5():
    """Находит все простые числа до N с помощью решета Эратосфена.
    Создаёт список и последовательно вычёркивает числа, кратные найденным простым"""
    n = int(input("Введите N: "))
    sieve = []
    
    for i in range(n + 1):
        sieve.append(True)
        
    sieve[0] = False
    sieve[1] = False
    i = 2
    while i * i <= n:
        if sieve[i]:
            j = i * i
            while j <= n:
                sieve[j] = False
                j = j + i
        i = i + 1

    primes = []
    for i in range(2, n + 1):
        if sieve[i]:
            primes.append(i)

    print("Простые числа в диапазоне [2, " + str(n) + "]:")
    print(primes)
    print("Всего найдено: " + str(len(primes)))

def task6():
    """Находит цифру на N-й позиции в бесконечной строке и 
    определяет длину нужного числа, вычисляет само число и извлекает из него конкретную цифру"""
    n = int(input("Введите позицию N: "))

    k = 1          # длина числа
    count = 9      # сколько k-значных чисел
    start = 1      # первое k-значное число

    while n > k * count:
        n = n - k * count
        k = k + 1
        count = count * 10
        start = start * 10

    number = start + (n - 1) // k
    digit_index = (n - 1) % k
    digit = str(number)[digit_index]
    print("Цифра на позиции: " + digit)

task1()
task2()
task3()
task4()
task5()
task6()