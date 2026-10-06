import random

def caesar_cipher(text, shift, mode="encode"):
    """Шифрует или дешифрует текст шифром Цезаря.
    Автоматически определяет язык каждого символа и сдвигает его в пределах своего алфавита,
    используя остаток от деления (%), чтобы символ 'зацикливался' и возвращался в начало."""
    result = ""
    # Если режим дешифровки, делаем сдвиг в обратную сторону
    if mode == "decode":
        shift = -shift

    for char in text:
        # Проверяем, является ли символ русской буквой
        if "а" <= char <= "я":
            base = ord("а")
            result += chr((ord(char) - base + shift) % 32 + base)
        elif "А" <= char <= "Я":
            base = ord("А")
            result += chr((ord(char) - base + shift) % 32 + base)
        # Проверяем, является ли символ английской буквой
        elif "a" <= char <= "z":
            base = ord("a")
            result += chr((ord(char) - base + shift) % 26 + base)
        elif "A" <= char <= "Z":
            base = ord("A")
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            # Пробелы и знаки препинания оставляем без изменений
            result += char
    return result

def check_winners(scores, student_score):
    """Определяет, входит ли балл студента в тройку лучших.
    Сортирует список баллов по убыванию и проверяет наличие балла в первых трёх элементах."""
    top_3 = sorted(scores, reverse=True)[:3]
    if student_score in top_3:
        print("Вы в тройке победителей!")
    else:
        print("Вы не попали в тройку победителей.")

def print_pack_report(n):
    """Перебирает числа от n до 1 и определяет варианты фасовки пирожных.
    Проверяет делимость на 3 и 5, чтобы вывести корректную инструкцию для каждого числа."""
    for i in range(n, 0, -1):
        if i % 3 == 0 and i % 5 == 0:
            print(f"{i} - расфасуем по 3 или по 5")
        elif i % 5 == 0:
            print(f"{i} - расфасуем по 5")
        elif i % 3 == 0:
            print(f"{i} - расфасуем по 3")
        else:
            print(f"{i} - не заказываем!")

def generate_complex_password():
    """Генерирует пароль с настраиваемыми параметрами.
    Запрашивает у пользователя длину и типы символов, формирует общий пул символов 
    и случайно выбирает из него символы до достижения нужной длины."""
    print("\n--- Генератор сложных паролей ---")
    length = int(input("Введите длину пароля: "))
    
    pool = ""
    if input("Использовать строчные буквы (a-z)? (д/н): ").lower() == "д":
        pool += "abcdefghijklmnopqrstuvwxyz"
    if input("Использовать заглавные буквы (A-Z)? (д/н): ").lower() == "д":
        pool += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if input("Использовать цифры (0-9)? (д/н): ").lower() == "д":
        pool += "0123456789"
    if input("Использовать спецсимволы (!@#$%^&*)? (д/н): ").lower() == "д":
        pool += "!@#$%^&*"
    
    if not pool:
        print("Вы не выбрали ни одного типа символов!")
        return

    password = ""
    for _ in range(length):
        # Случайно выбираем символ из собранного пула
        password += pool[random.randint(0, len(pool) - 1)]
    
    print(f"Ваш сгенерированный пароль: {password}")

def int_to_roman(num):
    """Конвертирует обычное число в римское.
    Последовательно вычитает максимальные возможные римские значения из числа, 
    добавляя соответствующие символы в результат."""
    val = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]
    result = ""
    for value, symbol in val:
        while num >= value:
            result += symbol
            num -= value
    return result

def roman_to_int(s):
    """Конвертирует римское число в обычное.
    Складывает значения символов, но вычитает текущее значение, если оно меньше следующего,
    чтобы корректно обработать случаи вроде IV (4) или IX (9)."""
    roman_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0
    for i in range(len(s)):
        # Если текущий символ меньше следующего, вычитаем его значение
        if i + 1 < len(s) and roman_map[s[i]] < roman_map[s[i + 1]]:
            result -= roman_map[s[i]]
        else:
            result += roman_map[s[i]]
    return result

def play_hangman():
    """Реализует игру 'Виселица'.
    Загадывает слово, принимает буквы от пользователя и отслеживает количество ошибок,
    завершая игру при угадывании слова или исчерпании попыток."""
    words = ["программа", "алгоритм", "функция", "переменная", "словарь"]
    word = random.choice(words)
    guessed = set()
    attempts = 6

    print("\n--- Игра 'Виселица' ---")
    print(f"Загадано слово из {len(word)} букв. У вас {attempts} попыток.")

    while attempts > 0:
        # Формируем отображение слова: угаданные буквы показываем, остальные заменяем на '_'
        display = [char if char in guessed else "_" for char in word]
        print(" ".join(display))

        if "_" not in display:
            print("Поздравляю, вы угадали слово!")
            return

        guess = input("Введите букву: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Пожалуйста, введите одну букву.")
            continue

        if guess in guessed:
            print("Вы уже называли эту букву.")
            continue

        guessed.add(guess)
        if guess not in word:
            attempts -= 1
            print(f"Неверно! Осталось попыток: {attempts}")

    print(f"Вы проиграли. Загаданное слово было: {word}")

# === Демонстрация работы всех задач ===
if __name__ == "__main__":
    print("\n1. Шифр Цезаря:")
    text = "Привет, World!"
    encrypted = caesar_cipher(text, 3, "encode")
    print(f"Оригинал: {text}\nЗашифровано: {encrypted}\nРасшифровано: {caesar_cipher(encrypted, 3, 'decode')}")

    print("\n2. Олимпиада:")
    check_winners([20, 48, 52, 38, 36, 13], 48)  # Должно быть в тройке
    check_winners([20, 48, 52, 38, 36, 13], 20)  # Не должно быть в тройке

    print("\n3. Пироженки (пример для n=12):")
    print_pack_report(12)

    print("\n4. Сложные пароли (запустится интерактивно, если раскомментировать):")
    # generate_complex_password()

    print("\n5. Римский конвертер:")
    print(f"42 в римские: {int_to_roman(42)}")
    print(f"XCIX в обычные: {roman_to_int('XCIX')}")

    print("\n6. Виселица (запустится интерактивно, если раскомментировать):")
    # play_hangman()