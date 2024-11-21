from src.lawn_grass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


def test_printing_mixin(capsys):
    Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    massage = capsys.readouterr()
    assert massage.out.strip() == "Product(Iphone 15, 512GB, Gray space, 210000.0, 8)"

    LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")
    massage = capsys.readouterr()
    assert massage.out.strip() == "LawnGrass(Газонная трава 2, Выносливая трава, 450.0, 15)"

    Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    massage = capsys.readouterr()
    assert massage.out.strip() == "Smartphone(Iphone 15, 512GB, Gray space, 210000.0, 8)"
