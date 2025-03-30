import pytest

from src.category import Category
# from src.product import Product


def test_category_init(category_1, category_2):
    """Тестируем работу инициализатора категорий и счётчиков"""
    assert category_1.name == "Смартфоны"
    assert (
        category_2.description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )

    assert Category.category_count == 2
    assert Category.product_count == 3


def test_category_products(category_2):
    """Тестируем работу метода products"""
    assert category_2.products == "'55' QLED 4K, 123000.0 руб. Остаток: 7 шт.\n"


def test_category_add_product(category_1, product_4):
    """Тестируем метод добавления продукта в категорию и обновление счётчика"""
    category_1.add_product(product_4)
    assert len(category_1.products_list) == 3
    assert Category.product_count == 3


def test_category_add_product_error(category_1):
    """Тестируем возврат ошибки, при добавлении несуществующего продукта"""
    with pytest.raises(TypeError):
        category_1.add_product("Not a product")
    assert Category.product_count == 2


def test_category_str(category_1):
    """Тестируем вывод строковой информации по категории"""
    expected_output = "Смартфоны, количество продуктов: 13 шт."
    assert str(category_1) == expected_output


def test_product_iterator(product_iterator):
    """Тестируем итератор списка продуктов"""
    iter(product_iterator)
    assert product_iterator.index == 0
    assert next(product_iterator).description == "256GB, Серый цвет, 200MP камера"
    assert product_iterator.index == 1
    assert next(product_iterator).description == "512GB, Gray space"

    with pytest.raises(StopIteration):
        next(product_iterator)


def test_middle_price(category_1, category_empty):
    """Тестируем подсчёт средней цены продукта в категории"""
    assert category_1.middle_price() == 195000.0
    assert category_empty.middle_price() == 0

#
# def test_my_exception(category_2, product_3, capsys):
#     assert product_3.quantity == 7
#
#     category_2.add_product(product_3)
#     message = capsys.readouterr()
#     assert message.out.strip().split('\n')[-1] == 'Работа метода завершена.'
#     assert message.out.strip().split('\n')[-2] == 'Товар добавлен успешно!'
#
#     product_5 = Product("Iphone 15", "512GB, Gray space", 210000.0, 0)
#     category_2.add_product(product_5)
#     message = capsys.readouterr()
#     assert message.out.strip().split('\n')[-1] == 'Работа метода завершена.'
#     assert message.out.strip().split('\n')[-2] == 'Нельзя добавить продукт с нулевым количеством!'
