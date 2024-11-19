# from unittest.mock import patch

from src.product import Product


def test_product_init(product_1, product_2, product_3):
    """Тестируем инициализацию продуктов"""
    assert product_1.name == "Samsung Galaxy S23 Ultra"
    assert product_1.description == "256GB, Серый цвет, 200MP камера"
    assert product_1.price == 180000.0
    assert product_3.quantity == 7


def test_product_new(product_1, product_2):
    """Тестируем метод добавления нового продукта из словаря"""
    new_product = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180.0,
            "quantity": 5,
        },
        [product_1, product_2],
    )

    assert new_product.name == "Samsung Galaxy S23 Ultra"
    assert new_product.quantity == 10
    assert new_product.price == 180000.0


def test_product_price_minus(product_3, capsys):
    """Тестируем функцию на возврат сообщения, при задании неверной цены"""
    product_3.price = -200
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"


def test_product_price(product_4):
    """Тестируем получение цены и ее изменение в различных сценариях"""
    assert product_4.price == 23000.0  # Отображение текущей цены

    product_4.price = 33000.0  # Повышение цены и ее возврат
    assert product_4.price == 33000.0


# @patch('builtins.input', side_effect=['y'])
# def test_set_price_decrease_yes(product_4):
#     product_4.price = 3300.0  # Понижение цены и ее возврат после вопроса пользователю и его ответа "да"
#     assert product_4.price == 3300.0
#
#
# @patch('builtins.input', side_effect=['n'])
# def test_set_price_decrease_no(product_4):
#     product_4.price = 3300.0  # Понижение цены и возврат старой после вопроса пользователю и его ответа "нет"
#     assert product_4.price == 23000.0


def test_product_str(product_2):
    """Тестируем метод предоставления строковой информации по продукту"""
    expected_output = "Iphone 15, 210000.0 руб. Остаток: 8 шт."
    assert str(product_2) == expected_output


def test_product_add(product_1, product_2):
    """Тестируем метод получения суммарной стоимости товаров"""
    expected_output = 2580000.0
    assert product_1 + product_2 == expected_output
