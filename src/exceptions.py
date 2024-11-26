class ZeroQuantityProduct(Exception):
    """Исключение для нулевого количества товара"""

    def __init__(self, message):
        super().__init__(message)
