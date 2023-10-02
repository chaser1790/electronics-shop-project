import pytest
from src.phone import Phone
from src.item import Item

class TestPhone:
    def test_init(self):
        """
        Тестирование инициализации экземпляров Phone.
        """
        phone = Phone("iPhone 14", 120000, 5, 2)
        assert phone.name == "iPhone 14"
        assert phone.price == 120000
        assert phone.quantity == 5
        assert phone.number_of_sim == 2
        assert phone in Item.all_items  # убедимся, что телефон добавлен в общий список товаров.

    def test_number_of_sim_setter(self):
        """
        Тестирование свойства number_of_sim (количество SIM-карт).
        """
        phone = Phone("iPhone 14", 120000, 5, 2)

        # Тест корректного задания количества SIM-карт
        phone.number_of_sim = 1
        assert phone.number_of_sim == 1

        # Тест задания некорректного количества SIM-карт
        with pytest.raises(ValueError) as excinfo:
            phone.number_of_sim = 0
        assert "Количество физических SIM-карт должно быть целым числом больше нуля." in str(excinfo.value)

    def test_repr(self):
        """
        Тестирование метода __repr__ класса Phone.
        """
        phone = Phone("iPhone 14", 120000, 5, 2)
        assert repr(phone) == "Phone('iPhone 14', 120000, 5, 2)"

    def test_add(self):
        """
        Тестирование метода __add__ класса Phone.
        """
        phone1 = Phone("iPhone 14", 120000, 5, 2)
        phone2 = Phone("Samsung Galaxy S21", 90000, 3, 2)
        item1 = Item("Charger", 2000, 10)

        # Тест сложения двух телефонов
        assert phone1 + phone2 == 8

        # Тест сложения телефона и другого товара
        assert phone1 + item1 == 15

        # Тест сложения телефона с не подходящим типом данных
        with pytest.raises(ValueError) as excinfo:
            result = phone1 + "test"
        assert "Только экземпляры класса Phone или Item могут быть сложены." in str(excinfo.value)
