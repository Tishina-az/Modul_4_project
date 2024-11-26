from src.base_order import BaseOrder
from src.product import Product


class Category(BaseOrder):
    """Класс представляет информацию по категориям товаров со списком товаров"""

    name: str
    description: str
    products: list

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        """Инициализатор категорий, содержит имя, описание и список товаров, обновляет счётчики категорий и товаров"""
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(self.__products)

    @property
    def products(self):
        """Метод, предоставляющий информацию по каждому товару в виде строки"""
        products_str = ""
        for prod in self.__products:
            products_str += f"{prod.name}, {prod.price} руб. Остаток: {prod.quantity} шт.\n"
        return products_str

    @property
    def products_list(self):
        return self.__products

    def add_product(self, new_product):
        """Метод для добавления нового товара в категорию"""
        if isinstance(new_product, Product):
            self.__products.append(new_product)
            Category.product_count += 1
        else:
            raise TypeError

    def __str__(self):
        """Строковое отображение информации по категории"""
        products_quantity = 0
        for prod in self.__products:
            products_quantity += prod.quantity
        return f"{self.name}, количество продуктов: {products_quantity} шт."

    def middle_price(self):
        """ Метод подсчета средней цены товара в категории"""
        try:
            avg_price = sum([product.price for product in self.__products]) / len(self.__products)
        except ZeroDivisionError:
            return 0
        else:
            return round(avg_price, 2)
