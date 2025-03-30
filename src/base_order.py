from abc import ABC, abstractmethod


class BaseOrder(ABC):
    """ Базовый класс для Заказа и Категорий """

    @abstractmethod
    def __str__(self):
        pass
