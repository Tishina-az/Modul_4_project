from src.category import Category


def test_product_init(product_1, product_2, product_3):
    assert product_1.name == "Samsung Galaxy S23 Ultra"
    assert product_1.description == "256GB, Серый цвет, 200MP камера"
    assert product_1.price == 180000.0
    assert product_3.quantity == 7
