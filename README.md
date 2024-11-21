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
3. Добавлены дочерние классы `Smartphone` и `LawnGrass` для класса `Product`, позволяющие добавлять продукты соответствующих категорий.
4. В классе `Product` прописаны методы:
   - магический метод `__str__`, возвращающий информацию по продукту в виде строки:
   ```
   Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.
   ```
   - метод `new_product` позволяет вернуть новый или обновленный продукт;
   - геттер `price` возвращает стоимость продукта, а сеттер `price` позволяет изменять стоимость продукта;
   - магический метод `__add__` служит для получения суммарной стоимости продуктов одного класса (например `смартфоны`).
5. В модуле `category.py`, расположен класс `Category`, обладающий следующими свойствами:
   - название (`name`),
   - описание (`description`),
   - список товаров категории (`products`).
6. В классе `Category` добавлено два атрибута количество категорий - `categories_count` и количество товаров - `products_count`.
7. В классе `Category` реализованы такие методы, как:
   - `products`, предоставляющий информацию по каждому товару категории;
   ```
   Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.
   Iphone 15, 210000.0 руб. Остаток: 8 шт.
   Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.
   ```
   - `products_list`, возвращающий список продуктов;
   - `add_product`, позволяющий добавить в категорию новый продукт, если он соответствует заданному классу;
   - также магический метод `__str__`, возвращающий информацию о категории, следующего вида:
   ```
   Смартфоны, количество продуктов: 200 шт.
   ```

## Документация:

*Раздел находится в разработке.*

## Лицензия:

*Раздел находится в разработке.*
