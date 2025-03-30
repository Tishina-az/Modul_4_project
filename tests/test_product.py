import unittest
from unittest.mock import patch

import pytest

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
    assert new_product.description == "256GB, Серый цвет, 200MP камера"


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


class TestProduct(unittest.TestCase):
    """Класс для тестирования изменения цены продукта"""
    product = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)

    def test_set_product_price_yes(self):
        with patch('builtins.input', return_value='y'):
            self.product.price = 80000.0
        self.assertEqual(self.product.price, 80000.0)

    def test_set_product_price_no(self):
        with patch('builtins.input', return_value='n'):
            current_price = self.product.price
            self.product.price = 80.0
        self.assertEqual(self.product.price, current_price)


def test_product_str(product_2):
    """Тестируем метод предоставления строковой информации по продукту"""
    expected_output = "Iphone 15, 210000.0 руб. Остаток: 8 шт."
    assert str(product_2) == expected_output


def test_product_add(product_1, product_2):
    """Тестируем метод получения суммарной стоимости товаров"""
    expected_output = 2580000.0
    assert product_1 + product_2 == expected_output


def test_product_add_error(smartphone_2, grass_2):
    """Тестируем метод получения суммарной стоимости товаров"""
    with pytest.raises(TypeError):
        assert smartphone_2 + grass_2


def test_product_add_empty():
    """Тестируем возвращение исключения при нулевом количестве товара"""
    with pytest.raises(ValueError):
        Product("Бракованный товар", "Неверное количество", 1000.0, 0)
