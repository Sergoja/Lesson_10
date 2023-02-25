from abs_storage import Storage


class Shop(Storage):
    def __init__(self, items: dict, capacity: int = 20):
        self.__items = items
        self.__capacity = capacity

    def add(self, name, quantity):
        if self.get_unique_items_count() > 5:
            print('Слишком много разных товаров')
            return

        if self.get_free_space() < quantity:
            print('Нет места')
            return

        if name in self.__items:
            self.__items[name] += quantity
        else:
            self.__items[name] = quantity

    def remove(self, name, quantity):
        if name not in self.__items:
            print('Нет такого')
            return

        if self.__items[name] < quantity:
            print('Не хватает товара')
            return

        self.__items[name] -= quantity

        if self.__items[name] == 0:
            self.__items.pop(name)

    def get_free_space(self):
        return self.__capacity - sum(self.__items.values())

    def get_items(self):
        return self.__items

    def get_unique_items_count(self):
        return len(self.__items)
