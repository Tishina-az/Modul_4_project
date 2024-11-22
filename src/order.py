from src.base_order import BaseOrder
from src.product import Product


class Order(BaseOrder):
    """ Класс представления заказа """
    order_count = 0

    def __init__(self, product: Product, quantity):
        """ Конструктор для класса Заказ """
        self.product = product
        self.quantity = quantity
        self.total_cost = self.product.price * self.quantity
        Order.order_count += 1

    def __str__(self):
        """ Строковое отображение информации по заказу """
        return f"""Вы заказали {self.product.name}, в количестве - {self.quantity} шт.
Общая стоимость заказа - {self.total_cost} рублей."""
