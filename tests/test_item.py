import pytest
import csv
import os
from src.item import Item, InstantiateCSVError


class TestItem:
    """Набор тестов для класса Item."""

    @pytest.fixture(autouse=True)
    def setup(self):
        Item.all_items = []
        Item.pay_rate = 1

    def test_init(self):
        """
        Тестирование правильности создания экземпляра класса Item.
        """
        item = Item("Смартфон", 10000, 20)
        assert item.name == "Смартфон"
        assert item.price == 10000
        assert item.quantity == 20
        assert item in Item.all_items

    def test_calculate_total_price(self):
        """
        Тестирование метода calculate_total_price.
        """
        item = Item("Смартфон", 10000, 20)
        total_price = item.calculate_total_price(pay_rate=1)
        assert total_price == 200000

    def test_apply_discount(self):
        """
        Тестирование метода apply_discount.
        """
        item = Item("Ноутбук", 20000, 5)
        Item.pay_rate = 0.8
        item.apply_discount(Item.pay_rate)
        assert item.price == 16000.0

    def test_rounded_price_after_discount(self):
        """
        Тестирование правильности округления стоимости товара после применения скидки.
        """
        item = Item("Компьютер", 15015.42, 3)
        Item.pay_rate = 0.629
        item.apply_discount(Item.pay_rate)
        assert item.price == 9444.7

    def test_all_items(self):
        """
        Тестирование правильности добавления и хранения созданных объектов класса Item.
        """
        item1 = Item("Смартфон", 10000, 20)
        item2 = Item(" Ноутбук", 20000, 5)
        assert len(Item.all_items) == 2
        assert item1 in Item.all_items
        assert item2 in Item.all_items

    def test_name_setter(self):
        """
        Тестирование сеттера имени товара.
        Ожидается исключение при превышении максимально допустимой длины имени товара.
        """
        item = Item('Телефон', 10000, 5)

        # длина наименования товара меньше 10 символов
        item.name = 'Смартфон'
        assert item.name == 'Смартфон'

        # длина наименования товара больше 10 символов
        with pytest.raises(Exception) as excinfo:
            item.name = 'СуперСмартфон'
        assert "Длина наименования товара превышает 10 символов." in str(excinfo.value)

    def test_instantiate_from_csv(self):
        """
        Тестирование метода instantiate_from_csv.
        """
        Item.instantiate_from_csv('src/items.csv')
        assert len(Item.all_items) == 5

    def test_string_to_number(self):
        """
        Тестирование метода string_to_number.
        """
        assert Item.string_to_number('5') == 5
        assert Item.string_to_number('5.0') == 5
        assert Item.string_to_number('5.5') == 5

    def test_repr(self):
        """
        Тестирование магического метода __repr__.
        """
        item = Item("Смартфон", 10000, 20)
        assert repr(item) == "Item('Смартфон', 10000, 20)"

    def test_str(self):
        """
        Тестирование магического метода __str__.
        """
        item = Item("Смартфон", 10000, 20)
        assert str(item) == "Смартфон"

    def test_instantiate_from_csv_missing_file(self):
        """
        Тестирование выброса исключения FileNotFoundError при попытке открыть отсутствующий файл.
        """
        try:
            Item.instantiate_from_csv('missing_file.csv')
        except FileNotFoundError as e:
            assert str(e) == 'Отсутствует файл item.csv'
        except Exception as e:
            pytest.fail(f"Поймано неправильное исключение: {e}")

    def test_instantiate_from_csv_corrupted_file(self):
        """
        Тестирование выброса исключения InstantiateCSVError при попытке прочитать поврежденный файл.
        """
        # Создание временного поврежденного файла
        with open('tmp.csv', 'w', newline='') as csvfile:
            fieldnames = ['name', 'price']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({'name': 'Смартфон', 'price': '100'})

        try:
            Item.instantiate_from_csv('tmp.csv')
        except InstantiateCSVError as e:
            assert str(e) == 'Файл item.csv поврежден'
        except Exception as e:
            pytest.fail(f"Поймано неправильное исключение: {e}")
        finally:
            # Удаление временного файла после теста
            os.remove('tmp.csv')
