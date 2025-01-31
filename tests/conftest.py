import pytest

from src.category import Category
from src.iterator import ProductIterator
from src.lawn_grass import LawnGrass
from src.order import Order
from src.product import Product
from src.smartphone import Smartphone


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
    return Product(
        name="Samsung Galaxy S23 Ultra", description="256GB, Серый цвет, 200MP камера", price=23000.0, quantity=3
    )


@pytest.fixture
def category_1(product_1, product_2):
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, "
        "но и получения дополнительных функций для удобства жизни",
        products=[product_1, product_2],
    )


@pytest.fixture
def category_2(product_3):
    return Category(
        name="Телевизоры",
        description="Современный телевизор, который позволяет наслаждаться просмотром, "
        "станет вашим другом и помощником",
        products=[product_3],
    )


@pytest.fixture
def product_iterator(category_1):
    return ProductIterator(category_1)


@pytest.fixture(autouse=True)
def reset_product_count():
    """Фикстура для обнуления product_count перед каждым тестом."""
    Category.product_count = 0


@pytest.fixture
def smartphone_1():
    return Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера",
        180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )


@pytest.fixture
def smartphone_2():
    return Smartphone("Iphone 15", "512GB, Gray space",
                      210000.0, 8, 98.2, "15", 512, "Gray space")


@pytest.fixture
def grass_1():
    return LawnGrass("Газонная трава", "Элитная трава для газона",
                     500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def grass_2():
    return LawnGrass("Газонная трава 2", "Выносливая трава",
                     450.0, 15, "США", "5 дней", "Темно-зеленый")


@pytest.fixture
def order_1(grass_1):
    return Order(grass_1, 5)


@pytest.fixture
def order_2(smartphone_2):
    return Order(smartphone_2, 2)
