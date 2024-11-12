import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def product_1():
    return Product(
        name="Samsung Galaxy S23 Ultra", description="256GB, Серый цвет, 200MP камера", price=180000.0, quantity=5
    )


@pytest.fixture
def product_2():
    return Product(name="Iphone 15", description="512GB, Gray space", price=210000.0, quantity=8)


@pytest.fixture
def product_3():
    return Product(name="'55' QLED 4K", description="Фоновая подсветка", price=123000.0, quantity=7)


@pytest.fixture
def product_4():
    return Product(name="Samsung Galaxy S23 Ultra", description="256GB, Серый цвет, 200MP камера", price=23000.0, quantity=3)


@pytest.fixture
def category_1(product_1, product_2):
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации,но и получения дополнительных функций для удобства жизни",
        products=[product_1, product_2]
    )


@pytest.fixture
def category_2(product_3):
    return Category(
        name="Телевизоры",
        description="Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        products=[product_3]
    )
