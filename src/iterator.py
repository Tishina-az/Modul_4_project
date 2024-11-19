class ProductIterator:
    """ Итератор, возвращающий поочередно продукты по заданной категории """

    def __init__(self, category_obj):
        """ Инициализатор итератора"""
        self.category = category_obj
        self.index = 0

    def __iter__(self):
        """ Магический метод, задающий стартовый индекс и возвращающий итератор """
        return self

    def __next__(self):
        """ Магический метод, возвращающий следующий элемент списка продуктов """
        if self.index < len(self.category.products_list):
            product = self.category.products_list[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration
