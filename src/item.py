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
        self.name = name
        self.price = price
        self.quantity = quantity
        Item.all_items.append(self)

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