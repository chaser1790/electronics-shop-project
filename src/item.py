import csv

class Item:
    def __init__(self, name, price, quantity):
        self._name = name
        self.price = price
        self.quantity = quantity

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) <= 10:
            self._name = value
        else:
            self._name = value[:10]
            raise Exception("Длина наименования товара превышает 10 символов.")

    @classmethod
    def instantiate_from_csv(cls, file_path):
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
        return int(float(string))