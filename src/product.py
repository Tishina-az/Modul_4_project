from src.base_product import BaseProduct
from src.printing_mixin import PrintingMixin


class Product(BaseProduct, PrintingMixin):
    """Класс, возвращающий объект продукта и информацию по нему"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Инициализатор, принимающий название, описание, цену и количество продукта"""
        self.name = name  # название
        self.description = description  # описание
        self.__price = price  # цена
        if quantity > 0:
            self.quantity = quantity  # количество в наличии
        else:
            raise ValueError('Товар с нулевым количеством не может быть добавлен.')
        super().__init__()

    def __str__(self):
        """Метод возвращающий информацию по продукту в строковом виде"""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    @classmethod
    def new_product(cls, product: dict, products: list):
        """Метод, возвращающий новый или обновленный продукт в виде объекта"""
        name, description, price, quantity = (value for value in product.values())
        for prod in products:
            if prod.name == name:
                prod.quantity += quantity
                prod.price = max(prod.price, price)
                return prod
        return cls(name, description, price, quantity)

    @property
    def price(self):
        """Геттер, возвращающий стоимость продукта"""
        return self.__price

    @price.setter
    def price(self, new_price):
        """Сеттер для изменения стоимости продукта и проверки валидности"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            if new_price < self.__price:
                user_answer = input("Подтвердите снижение цены (Y/N): ")
                if user_answer.lower() == "y":
                    self.__price = new_price
            else:
                self.__price = new_price

    def __add__(self, other):
        """Метод для получения общей стоимости продуктов"""
        if type(other) is self.__class__:
            result = self.__price * self.quantity + other.price * other.quantity
            return result
        else:
            raise TypeError
