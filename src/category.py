class Category:
    name: str
    description: str
    products: list

    categories_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.categories_count += 1
        Category.product_count += len(products)

    @property
    def products(self):
        products_str = ""
        for prod in self.__products:
            products_str += f"{prod.name}, {prod.price} руб. Остаток: {prod.quantity} шт.\n"
        return products_str

    def add_product(self, new_product):
        self.__products.append(new_product)
        Category.product_count += 1
