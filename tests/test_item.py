import unittest
from src.item import Item


class TestItem(unittest.TestCase):
    """Набор тестов для класса Item."""

    def setUp(self):
        Item.all_items = []
        Item.pay_rate = 1

    def test_init(self):
        """
        Тестирование правильности создания экземпляра класса Item.
        """
        item = Item("Смартфон", 10000, 20)
        self.assertEqual(item.name, "Смартфон")
        self.assertEqual(item.price, 10000)
        self.assertEqual(item.quantity, 20)
        self.assertIn(item, Item.all_items)

    def test_calculate_total_price(self):
        """
        Тестирование метода calculate_total_price.
        """
        item = Item("Смартфон", 10000, 20)
        total_price = item.calculate_total_price(pay_rate=1)
        self.assertEqual(total_price, 200000)

    def test_apply_discount(self):
        """
        Тестирование метода apply_discount.
        """
        item = Item("Ноутбук", 20000, 5)
        Item.pay_rate = 0.8
        item.apply_discount(Item.pay_rate)

        self.assertEqual(item.price, 16000.0)

    def test_rounded_price_after_discount(self):
        """
        Тестирование правильности округления стоимости товара после применения скидки.
        """
        item = Item("Компьютер", 15015.42, 3)
        Item.pay_rate = 0.629
        item.apply_discount(Item.pay_rate)

        self.assertEqual(item.price, 9444.7)

    def test_all_items(self):
        """
        Тестирование правильности добавления и хранения созданных объектов класса Item.
        """
        item1 = Item("Смартфон", 10000, 20)
        item2 = Item(" Ноутбук", 20000, 5)

        self.assertEqual(len(Item.all_items), 2)
        self.assertIn(item1, Item.all_items)
        self.assertIn(item2, Item.all_items)


if __name__ == '__main__':
    unittest.main()