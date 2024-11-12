from src.category import Category
from tests.conftest import category_1, product_4


def test_category_init(category_1, category_2):
    assert category_1.name == "Смартфоны"
    assert (
        category_2.description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )

    assert Category.categories_count == 2
    assert Category.product_count == 3


def test_category_products(category_2):
    assert category_2.products == "'55' QLED 4K, 123000.0 руб. Остаток: 7 шт.\n"


# def test_category_add_product(category_1, product_4):
#     category_1.add_product(product_4)
#     assert Category.product_count == 3
