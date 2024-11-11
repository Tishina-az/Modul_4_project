class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product: dict, products: list):
        name, description, price, quantity = (value for value in product.values())
        for prod in products:
            if prod.name == name:
                prod.quantity += quantity
                prod.price = max(prod.price, price)
                return prod
        return cls(name, description, price, quantity)
