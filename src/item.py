import csv

class InstantiateCSVError(Exception):
    """Класс исключения, указывающего на ошибки при создании объектов из csv-файла."""
    pass

class Item:
    """Класс, представляющий товар."""

    pay_rate = 1  # уровень цен с учетом скидки
    all_items = []  # список всех созданных объектов класса Item

    def __init__(self, name, price, quantity):
        """
        Инициализация объекта класса Item.
        :param name: Название товара (str)
        :param price: Цена товара (float)
        :param quantity: Количество товара (int)
        """
        self._name = name
        self.price = round(float(price), 2)
        self.quantity = int(quantity)
        Item.all_items.append(self)

    @property
    def name(self):
        """Свойство для получения названия товара."""
        return self._name

    @name.setter
    def name(self, value):
        """
        Свойство для установки названия товара с проверкой на максимальное
        количество символов (10).
        :param value: Новое название товара (str)
        """
        if len(value) <= 10:
            self._name = value
        else:
            self._name = value[:10]
            raise Exception("Длина наименования товара превышает 10 символов.")

    def calculate_total_price(self, pay_rate):
        """
        Рассчитать общую стоимость товара с учетом количества и уровня цен.
        :param pay_rate: Уровень цен с учетом скидки (float)
        :return: Общая стоимость товара (float)
        """
        return self.price * self.quantity * pay_rate

    def apply_discount(self, pay_rate):
        """
        Применить скидку к товару, обновляя его стоимость.
        :param pay_rate: Уровень цен с учетом скидки (float)
        """
        self.price = self.price * pay_rate
        self.price = round(self.price, 2)

    @classmethod
    def instantiate_from_csv(cls, file_path='D:\\electronics-shop-project\\src\\items.csv'):
        """
        Создание объектов класса Item на основе данных из csv-файла.
        :param file_path: Путь к csv-файлу (str)
        """
        try:
            items = []
            with open(file_path, newline='') as csvfile:
                reader = csv.DictReader(csvfile)

                if set(reader.fieldnames) != {'name', 'price', 'quantity'}:
                    raise InstantiateCSVError('Файл item.csv поврежден')

                for row in reader:
                    try:
                        # Пытаемся преобразовать значения каждого поля к нужному типу.
                        # Если какое-то из полей пустое или его значение неверно, вызываем исключение ValueError.
                        name = row['name']
                        price = float(row['price']) if row['price'] else None
                        quantity = int(row['quantity']) if row['quantity'] else None
                        if not all([name, price, quantity]):
                            raise ValueError
                        item = cls(name, price, quantity)
                        items.append(item)
                    except ValueError:
                        # Если в процессе чтения и преобразования данных возникла ошибка, делаем вывод, что файл поврежден.
                        raise InstantiateCSVError('Файл item.csv поврежден')

                cls.all_items = items
        except FileNotFoundError:
            raise FileNotFoundError('Отсутствует файл item.csv')

    @staticmethod
    def string_to_number(string):
        """
        Преобразование числа в виде строки в целочисленное значение.
        :param string: Число в виде строки (str)
        :return: Число в виде целого числа (int)
        """
        return int(float(string))

    def __repr__(self):
        """
        Магический метод для представления объекта класса в форме строки,
        которую можно использовать для повторного создания объекта.
        :return: Строка в формате "Item('name', price, quantity)"
        """
        return f"Item('{self._name}', {int(self.price)}, {self.quantity})"

    def __str__(self):
        """
        Магический метод для представления объекта класса в виде удобочитаемой строки.
        :return: Название товара (str)
        """
        return self._name

    def __add__(self, other):
        """
        Сложение двух товаров по их количеству.
        :param other: другой объект класса Item.
        :return: сумма количеств товаров.
        """
        if not isinstance(other, Item):
            raise ValueError("Только экземпляры класса Item могут быть сложены.")
        return self.quantity + other.quantity