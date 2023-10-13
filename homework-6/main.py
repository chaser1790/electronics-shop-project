from src.item import Item, InstantiateCSVError

if __name__ == '__main__':
    try:
        # Пытаемся считать данные из файла items.csv
        Item.instantiate_from_csv()
    except FileNotFoundError as e:
        # Если файл не найден, выводим сообщение об ошибке
        print(str(e))
    except InstantiateCSVError as e:
        # Если файл поврежден, выводим сообщение об ошибке
        print(str(e))