from src.product import Product


class Smartphone(Product):
    """Смартфоны"""

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency  # производительность
        self.model = model  # модель
        self.memory = memory  # объем встроенной памяти
        self.color = color  # цвет
