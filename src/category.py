class Category:
    name: str
    description: str
    products: list

    categories_count = 0
    products_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        Category.categories_count += len(products)
