import csv

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
    def instantiate_from_csv(cls, file_path):
        """
        Создание объектов класса Item на основе данных из csv-файла.
        :param file_path: Путь к csv-файлу (str)
        """
        items = []
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                name = row['name']
                price = float(row['price'])
                quantity = int(row['quantity'])
                item = cls(name, price, quantity)
                items.append(item)
        cls.all = items

    @staticmethod
    def string_to_number(string):
        """
        Преобразование числа в виде строки в целочисленное значение.
        :param string: Число в виде строки (str)
        :return: Число в виде целого числа (int)
        """
        return int(float(string))
