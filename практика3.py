# Задача 1
class Book:
    """Класс, описывающий обычную книгу."""
    
    def __init__(self, title, author, year):
        # Чтобы сохранить данные о книге в атрибуты.
        self.title = title
        self.author = author
        self.year = year

    def info(self):
        """Возвращает строку с информацией о книге."""
        return f"Книга: '{self.title}', автор: {self.author}, год: {self.year}"

print(Book("Мастер и Маргарита", "Булгаков", 1940).info())


# Задача 2
class Ebook(Book):
    """Класс электронной книги, наследующий базовый класс Book."""
    
    def __init__(self, title, author, year, format):
        # Чтобы не дублировать код инициализации из родителя.
        super().__init__(title, author, year)
        self.format = format

    def info(self):
        """Переопределенный метод для вывода информации с учетом формата."""
        return f"Электронная книга: '{self.title}', автор: {self.author}, год: {self.year}, формат: {self.format}"

print(Ebook("1984", "Оруэлл", 1949, "PDF").info())


# Задача 3
from datetime import datetime

class BookExtended:
    """Класс книги с расширенными возможностями."""
    
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def info(self):
        return f"Книга: '{self.title}', автор: {self.author}, год: {self.year}"

    def __str__(self):
        # Чтобы при выводе print() не показывался адрес в памяти.
        return self.info()

    def __eq__(self, other):
        # Чтобы сравнение через == работало по названию и автору.
        if isinstance(other, BookExtended):
            return self.title == other.title and self.author == other.author
        return False

    @property
    def age(self):
        # Чтобы вычислять возраст на лету.
        return datetime.now().year - self.year

    @age.setter
    def age(self, value):
        # Чтобы автоматически пересчитывать год издания при смене возраста.
        self.year = datetime.now().year - value

    @classmethod
    def from_string(cls, data):
        # Чтобы создавать объект из строки без вызова конструктора напрямую.
        title, author, year = data.split(';')
        return cls(title, author, int(year))

print(BookExtended("Гарри Поттер", "Роулинг", 1997))
print(BookExtended("Гарри Поттер", "Роулинг", 1997) == BookExtended.from_string("Гарри Поттер;Роулинг;1997"))
print(BookExtended("Гарри Поттер", "Роулинг", 1997).age)


# Задача 4
from abc import ABC, abstractmethod

class Printable(ABC):
    """Абстрактный класс для печати."""
    
    @abstractmethod
    def print_info(self):
        # Чтобы обязать дочерние классы реализовать этот метод.
        pass

class PrintableBook(Printable):
    """Класс книги, реализующий абстрактный метод."""
    
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def print_info(self):
        # Чтобы выполнить требование абстрактного класса.
        print(f"Печать книги: {self.title} (автор: {self.author})")

PrintableBook("Война и мир", "Толстой").print_info()


# Практика 1
class Employee:
    """Базовый класс для сотрудника."""
    
    def __init__(self, id, name, base_money):
        self.id = id
        self.name = name
        self.base_money = base_money
    
    def calculate_salary(self):
        # Чтобы вернуть базовую ставку.
        return self.base_money

class Manager(Employee):
    """Класс менеджера."""
    
    def __init__(self, id, name, base_money, bonus):
        # Чтобы инициализировать базовые поля через родителя.
        super().__init__(id, name, base_money)
        self.bonus = bonus
    
    def calculate_salary(self):
        # Чтобы прибавить бонус к базовой ставке.
        return super().calculate_salary() + self.bonus

class Developer(Employee):
    """Класс разработчика."""
    
    def __init__(self, id, name, base_money, projects=0):
        super().__init__(id, name, base_money)
        self.projects = projects
    
    def calculate_salary(self):
        # Чтобы прибавить премию за каждый проект к базовой ставке.
        return super().calculate_salary() + (self.projects * 10000)

print(f"Иван: {Employee(1, 'Иван', 20000).calculate_salary()}")
print(f"Алекс: {Manager(2, 'Алекс', 20000, 5000).calculate_salary()}")
print(f"Григо: {Developer(3, 'Григо', 20000, 5).calculate_salary()}")


# Практика 2
class Transport:
    """Базовый класс для любого транспорта."""
    
    def __init__(self, name):
        self.name = name

    def description(self):
        # Чтобы вернуть базовое описание, если наследник не переопределил его.
        return f"Транспорт: {self.name}"

class Car(Transport):
    """Класс автомобиля."""
    def description(self):
        # Чтобы вернуть описание, характерное именно для машины.
        return f"{self.name} — это машина. У неё есть колёса, и она ездит по дорогам."

class Plane(Transport):
    """Класс самолета."""
    def description(self):
        # Чтобы вернуть описание, характерное именно для самолета.
        return f"{self.name} — это самолет. У него есть крылья, и он летает в небе."

class Bike(Transport):
    """Класс мотоцикла."""
    def description(self):
        # Чтобы вернуть описание, характерное именно для мотоцикла.
        return f"{self.name} — это мотоцикл. У него есть колёса, он небольшой, но быстрый."

print(Car("Toyota Camry").description())
print(Plane("Boeing 737").description())
print(Bike("ИЖ Юпитер").description())


# Практика 3
class Product:
    """Товар в магазине."""
    
    def __init__(self, name, price, stock, category):
        self.name = name
        self.price = price
        self.stock = stock
        self.category = category

    def __str__(self):
        # Чтобы при печати объекта выводилось название и цена.
        return f"{self.name} ({self.price} руб.)"

class Customer:
    """Покупатель магазина."""
    
    def __init__(self, name):
        self.name = name
        # Чтобы хранить историю всех заказов клиента.
        self.history = []

    def add_order(self, order):
        # Чтобы сохранить оформленный заказ в историю.
        self.history.append(order)

class ShoppingCart:
    """Корзина для покупок."""
    
    def __init__(self):
        # Чтобы хранить товары в формате {товар: количество}.
        self.items = {}

    def add_product(self, product, quantity=1):
        """Добавляет товар в корзину."""
        if product.stock >= quantity:
            self.items[product] = self.items.get(product, 0) + quantity
            product.stock -= quantity
            print(f"Товар '{product.name}' добавлен в корзину (x{quantity})")
        else:
            print(f"Недостаточно товара '{product.name}' на складе!")

    def remove_product(self, product, quantity=1):
        """Удаляет товар из корзины."""
        if product in self.items:
            if self.items[product] > quantity:
                self.items[product] -= quantity
                product.stock += quantity
            else:
                # Чтобы вернуть остаток товара на склад.
                product.stock += self.items[product]
                del self.items[product]
            print(f"Товар '{product.name}' удален из корзины.")

    def total_price(self):
        # Чтобы просуммировать цену каждого товара с учетом количества.
        return sum(p.price * q for p, q in self.items.items())

class Order:
    """Заказ."""
    
    def __init__(self, customer, cart, discount=0.0, tax=0.0):
        self.customer = customer
        # Чтобы скопировать товары из корзины в заказ.
        self.items = cart.items.copy()
        self.subtotal = cart.total_price()
        # Чтобы посчитать итоговую сумму со скидкой и налогом.
        self.total = self.subtotal * (1 - discount) * (1 + tax)

    def checkout(self):
        """Завершает оформление заказа."""
        # Чтобы добавить текущий заказ в историю покупателя.
        self.customer.add_order(self)
        print(f"Заказ для {self.customer.name} оформлен. Сумма: {round(self.total, 2)} руб.")

customer = Customer("Иван")
cart = ShoppingCart()
cart.add_product(Product("Яблоки", 100, 50, "Фрукты"), 3)
cart.add_product(Product("Хлеб", 50, 20, "Выпечка"), 2)
Order(customer, cart, discount=0.1, tax=0.05).checkout()


# Практика 4
class CrewMember:
    """Член экипажа."""
    
    def __init__(self, name, role, health=100):
        self.name = name
        self.role = role
        self.health = health

    def __str__(self):
        # Чтобы при печати выводились роль, имя и здоровье.
        return f"{self.role} {self.name} (здоровье: {self.health}%)"

class SpaceShip:
    """Космический корабль."""
    
    def __init__(self, name, fuel=100, hull_integrity=100):
        self.name = name
        self.fuel = fuel
        self.hull_integrity = hull_integrity
        self.speed = 0
        # Чтобы хранить список членов экипажа на борту.
        self.crew = []

    def add_crew(self, member):
        # Чтобы добавить нового члена в экипаж.
        self.crew.append(member)

    def accelerate(self, amount):
        """Ускоряет корабль."""
        if self.fuel >= amount:
            # Чтобы потратить топливо и увеличить скорость.
            self.fuel -= amount
            self.speed += amount * 10
            print(f"{self.name} ускоряется до {self.speed} км/с. Остаток топлива: {self.fuel}%")
        else:
            print(f"{self.name}: Недостаточно топлива для маневра!")

class Mission:
    """Космическая миссия."""
    
    def __init__(self, name, target, ship):
        self.name = name
        self.target = target
        self.ship = ship
        # Чтобы записывать историю событий в миссии.
        self.events = []

    def start(self):
        """Начинает миссию."""
        # Чтобы вывести данные о миссии и экипаже.
        print(f"Миссия '{self.name}' началась. Цель: {self.target}.")
        print(f"Корабль: {self.ship.name}")
        print("Экипаж на борту:")
        for member in self.ship.crew:
            print(f" - {member}")

    def trigger_event(self, event_type):
        """Симулирует событие."""
        if event_type == "asteroid":
            # Чтобы уменьшить целостность корпуса при столкновении.
            self.ship.hull_integrity -= 30
            print(f"Встреча с астероидом! Целостность корпуса: {self.ship.hull_integrity}%")
        elif event_type == "malfunction":
            print("Поломка двигателя! Требуется ремонт инженером.")
        
        # Чтобы сохранить произошедшее событие в историю.
        self.events.append(event_type)

ship = SpaceShip("Аврора")
ship.add_crew(CrewMember("Иван", "Пилот"))
ship.add_crew(CrewMember("Мария", "Инженер"))
mission = Mission("Поиск жизни", "Марс", ship)
mission.start()
ship.accelerate(20)
mission.trigger_event("asteroid")
