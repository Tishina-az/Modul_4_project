from unittest.mock import patch

from src.product import Product
from tests.conftest import product_4, product_3


def test_product_init(product_1, product_2, product_3):
    """ Тестируем инициализацию продуктов """
    assert product_1.name == "Samsung Galaxy S23 Ultra"
    assert product_1.description == "256GB, Серый цвет, 200MP камера"
    assert product_1.price == 180000.0
    assert product_3.quantity == 7


def test_product_new(product_1, product_2):
    """ Тестируем метод добавления нового продукта из словаря """
    new_product = Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180.0,
         "quantity": 5}, [product_1, product_2])

    assert new_product.name == "Samsung Galaxy S23 Ultra"
    assert new_product.quantity == 10
    assert new_product.price == 180000.0


def test_product_price_minus(product_3, capsys):
    """ Тестируем функцию на возврат сообщения, при задании неверной цены"""
    product_3.price = -200
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"


@patch('builtins.input')
def test_product_price(mock_input, product_4):
    """ Тестируем получение цены и ее изменение в различных сценариях """
    assert product_4.price == 23000.0   # Отображение текущей цены

    product_4.price = 33000.0           # Повышение цены и ее возврат
    assert product_4.price == 33000.0

    product_4.price = 3300.0            # Понижение цены и ее возврат после вопроса пользователю и его ответа "да"
    mock_input.side_effect = ''
    assert product_4.price == 3300.0
