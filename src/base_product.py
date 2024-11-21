from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """ Базовый класс для всех продуктов """

    @abstractmethod
    def __str__(self):
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs):
        return cls
