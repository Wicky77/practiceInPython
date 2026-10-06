import random

def caesar_cipher():
    """Шифрует или расшифровывает текст шифром Цезаря. Сдвигает буквы в пределах алфавита,
      используя остаток от деления%, чтобы буква зацикливалась и возвращалась в начало"""
    text = input("Введите текст: ")
    shift = int(input("Введите сдвиг: "))
    mode = input("Шифровать или расшифровать? (encode/decode): ")

    if mode == "decode":
        shift = -shift

    result = ""
    for char in text:
        if "а" <= char <= "я":
            base = ord("а")
            result += chr((ord(char) - base + shift) % 32 + base)
        elif "А" <= char <= "Я":
            base = ord("А")
            result += chr((ord(char) - base + shift) % 32 + base)
        elif "a" <= char <= "z":
            base = ord("a")
            result += chr((ord(char) - base + shift) % 26 + base)
        elif "A" <= char <= "Z":
            base = ord("A")
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    print("Результат: " + result)

def check_winners(scores, student_score):
    """Определяет, вошёл ли студент в тройку лидеров.
    Сортируем баллы по убыванию и берём первые 3, чтобы проверить наличие балла студента"""
    top_3 = sorted(scores, reverse=True)[:3]
    if student_score in top_3:
        print("Вы в тройке победителей!")
    else:
        print("Вы не попали в тройку победителей.")

def print_pack_report(n):
    """Выводит варианты фасовки пирожных для чисел от n до 1.
    Перебираем числа в обратном порядке и проверяем делимость, чтобы узнать варианты упаковки"""
    for i in range(n, 0, -1):
        if i % 3 == 0 and i % 5 == 0:
            print(str(i) + " - расфасуем по 3 или по 5")
        elif i % 5 == 0:
            print(str(i) + " - расфасуем по 5")
        elif i % 3 == 0:
            print(str(i) + " - расфасуем по 3")
        else:
            print(str(i) + " - не заказываем!")

def generate_complex_password():
    """Генерирует пароль по настройкам пользователя.
    Собираем общий набор символов на основе выбора, чтобы случайно выбирать из него нужное количество раз"""
    print("\n--- Генератор паролей ---")
    length = int(input("Введите длину пароля: "))

    pool = ""
    if input("Использовать строчные буквы (a-z)? (y/n): ").lower() == "y":
        pool += "abcdefghijklmnopqrstuvwxyz"
    if input("Использовать заглавные буквы (A-Z)? (y/n): ").lower() == "y":
        pool += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if input("Использовать цифры (0-9)? (y/n): ").lower() == "y":
        pool += "0123456789"
    if input("Использовать спецсимволы (!@#$%^&*)? (y/n): ").lower() == "y":
        pool += "!@#$%^&*"

    if pool == "":
        print("Вы не выбрали ни одного типа символов!")
        return

    password = ""
    for _ in range(length):
        password += pool[random.randint(0, len(pool) - 1)]

    print("Ваш пароль: " + password)

def int_to_roman():
    """Конвертирует обычное число в римcкcое.Последовательно вычитаем максимальные возможные
      римские значения из числа, добавляя символы в результат"""
    num = int(input("Введите число: "))
    values = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]
    result = ""
    for value, symbol in values:
        while num >= value:
            result += symbol
            num -= value
    print("Римское число: " + result)

def roman_to_int():
    """Конвертирует римское число в обычное. Вычитаем текущее значение, 
    если оно меньше следующего, чтобы правильно обработать римские 4 и 9"""
    s = input("Введите римское число: ").upper()
    roman_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0
    for i in range(len(s)):
        if i + 1 < len(s) and roman_map[s[i]] < roman_map[s[i + 1]]:
            result -= roman_map[s[i]]
        else:
            result += roman_map[s[i]]
    print("Обычное число: " + str(result))

def play_hangman():
    """Реализуем игру Виселица.
    Показываем угаданные буквы, а вместо остальных ставим _, чтобы игрок видел прогресс"""
    words = ["программа", "алгоритм", "функция", "переменная", "словарь"]
    word = random.choice(words)
    guessed = []
    attempts = 6

    print("\n--- Виселица ---")
    print("У вас " + str(attempts) + " попыток.")

    while attempts > 0:
        display = ""
        for char in word:
            if char in guessed:
                display += char + " "
            else:
                display += "_ "
        print(display)

        if "_" not in display:
            print("Вы угадали слово!")
            return

        guess = input("Введите букву: ").lower()

        if guess in guessed:
            print("Вы уже называли эту букву.")
            continue

        guessed.append(guess)
        if guess not in word:
            attempts -= 1
            print("Неверно! Осталось: " + str(attempts))

    print("Вы проиграли. Слово было: " + word)

caesar_cipher()
check_winners([20, 48, 52, 38, 36, 13], 48)
print_pack_report(12)
generate_complex_password()
int_to_roman()
roman_to_int()
play_hangman()