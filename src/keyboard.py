from .item import Item


class LanguageMixin:
    """
    Миксин для добавления свойства языка и метода изменения языка
    в дочерний класс. Используется для реализации мультиязычных
    клавиатур.

    Attributes:
        _language (str): Текущий выбранный язык.
    """

    def __init__(self, language="EN"):
        """
        Инициализация миксина с заданным языком (по умолчанию английский).

        Args:
            language (str): Индекс языка. По умолчанию "EN"
        """
        self._language = language

    @property
    def language(self):
        """
        Свойство для получения текущего языка клавиатуры.

        Returns:
            str: Текущий выбранный язык.
        """
        return self._language

    def change_lang(self):
        """
        Метод для переключения языка клавиатуры между русским (RU)
        и английским (EN).
        """
        if self._language == "EN":
            self._language = "RU"  # Переключение на русский язык
        else:
            self._language = "EN"  # Возвращение к английскому


class Keyboard(Item, LanguageMixin):
    """
    Класс объекта "Клавиатура", наследуется от класса "Товар"
    и миксина "Многоязычность".

    Attributes:
        name (str): Название клавиатуры.
        price (float): Цена за единицу.
        quantity (int): Количество единиц в наличии.
        _language (str): Текущий выбранный язык.
    """

    def __init__(self, name: str, price: float, quantity: int):
        """
        Инициализация класса Keyboard.

        Args:
            name (str): Название клавиатуры.
            price (float): Цена за единицу.
            quantity (int): Количество единиц в наличии.
        """
        Item.__init__(self, name, price, quantity)
        LanguageMixin.__init__(self)
