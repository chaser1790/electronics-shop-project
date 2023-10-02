from src.item import Item

class Phone(Item):
    """Класс, представляющий телефон, унаследованный от класса Item."""
    ...


    def __init__(self, name, price, quantity, number_of_sim):
        """
        Инициализация объекта класса Phone.
        :param name: Название телефона (str)
        :param price: Цена телефона (float)
        :param quantity: Количество телефонов (int)
        :param number_of_sim: Количество поддерживаемых SIM-карт (int)
        """
        super().__init__(name, price, quantity)
        if number_of_sim < 1:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
        self._number_of_sim = number_of_sim

    @property
    def number_of_sim(self):
        """Свойство для получения количества поддерживаемых SIM-карт."""
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value):
        """Свойство для установки количества поддерживаемых SIM-карт."""
        if value < 1:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
        self._number_of_sim = value

    def __repr__(self):
        """
        Магический метод для представления объекта класса в форме строки,
        которую можно использовать для повторного создания объекта.
        :return: Строка в формате "Phone('name', price, quantity, number_of_sim)"
        """
        return f"Phone('{self.name}', {int(self.price)}, {self.quantity}, {self.number_of_sim})"

    def __add__(self, other):
        """
        Сложение двух телефонов или телефона и товара по их количеству.
        :param other: другой объект класса Phone или Item.
        :return: сумма количеств телефонов и/или товаров.
        """
        if not isinstance(other, Item):
            raise ValueError("Только экземпляры класса Phone или Item могут быть сложены.")
        return self.quantity + other.quantity
