from src.item import Item

if __name__ == '__main__':
    # Создаем экземпляры класса Item: смартфон и ноутбук
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)

    pay_rate = 1  # Устанавливаем коэффициент оплаты в 1 (без скидки)

    # Выводим общую стоимость каждого элемента (цена x количество)
    print(item1.calculate_total_price(pay_rate))  # 200000
    print(item2.calculate_total_price(pay_rate))  # 100000

    # Устанавливаем новый уровень цен с коэффициентом 0.8 (20% скидки)
    Item.pay_rate = 0.8
    # Применяем скидку к смартфону
    item1.apply_discount(Item.pay_rate)

    # Выводим обновленные цены товаров
    print(item1.price)  # 8000.0
    print(item2.price)  # 20000

    # Выводим список всех созданных товаров
    print(Item.all_items)  # [<Item Смартфон>, <Item Ноутбук>]