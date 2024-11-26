from src.order import Order


def test_order_init(order_1):
    """ Тестируем конструктор """
    assert order_1.product.name == "Газонная трава"
    assert order_1.quantity == 5
    assert order_1.total_cost == 2500.0
    Order.order_count = 1


def test_order_str(order_2):
    """ Тестируем возвращение строки """
    expected_output = """Вы заказали Iphone 15, в количестве - 2 шт.
Общая стоимость заказа - 420000.0 рублей."""
    assert str(order_2) == expected_output
