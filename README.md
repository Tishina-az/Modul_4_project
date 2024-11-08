# Проект 'E-commerce - функционал'

## Описание:

E-commerce  — электронная торговля, или электронная коммерция.

## Установка:

1. Клонируйте репозиторий:
    [GitHub](<https://github.com/Tishina-az/Modul_4_project.git>)
    ```
    git clone
    ```
2. Установите зависимости из файла `pyproject.toml` с помощью команды:
    ```
    poetry install
    ```

## Функционал проекта:

1. Основная функция `main`, расположенная в модуле `main.py`, позволяет протестировать использование всего функционала.
2. В модуле `product.py`, расположен класс `Product`, обладающий следующими свойствами:
   - название (`name`),
   - описание (`description`),
   - цена (`price`),
   - количество в наличии (`quantity`).
3. В модуле `category.py`, расположен класс `Category`, обладающий следующими свойствами:
   - название (`name`),
   - описание (`description`),
   - список товаров категории (products).
4. В классе `Category` добавлено два атрибута количество категорий - `categories_count` и количество товаров - `products_count`.

## Документация:

*Раздел находится в разработке.*

## Лицензия:

*Раздел находится в разработке.*
