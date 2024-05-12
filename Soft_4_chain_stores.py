# Ты разрабатываешь программное обеспечение для сети магазинов. Каждый магазин в этой сети имеет свои особенности,
# но также существуют общие характеристики, такие как адрес, название и ассортимент товаров. Ваша задача — создать класс Store,
# который можно будет использовать для создания различных магазинов.
# Шаги: 1. Создай класс Store: Атрибуты класса:
# name: название магазина.
# address: адрес магазина.
# items: словарь, где ключ - название товара, а значение - его цена. Например, {'apples': 0.5, 'bananas': 0.75}.
# Методы класса:
# __init__ - конструктор, который инициализирует название и адрес, а также пустой словарь дляitems`.
# метод для добавления товара в ассортимент.
# метод для удаления товара из ассортимента.
# метод для получения цены товара по его названию. Если товар отсутствует, возвращайте None.
# метод для обновления цены товара.
# Шаг 2. Создай несколько объектов класса Store:
# Создай не менее трех различных магазинов с разными названиями, адресами и добавь в каждый из них несколько товаров.
class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}  # Инициализация пустого словаря для товаров
    def add_item(self, item_name, price):
        self.items[item_name] = price # Добавление нового товара-значения и ключа-цены
        print(f"Товар {item_name} добавлен в ассортимент магазина {self.name}")
    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f"Товар {item_name} удален из ассортимента магазина {self.name}")
    def get_price(self, item_name):
        return self.items.get(item_name, None)
        print(f"Цена {item_name} в магазине {self.name} - {self.items[item_name]}")
    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"Цена {item_name} в магазине {self.name} изменена на {new_price}")
        else:
            print(f"Товар {item_name} отсутствует в ассортименте магазина {self.name}")
# Создание объектов класса Store
store1 = Store("Магазин Плюс", "Улица Лесная, 5")
store1.add_item("яблоки", 50)
store1.add_item("бананы", 25)
store1.add_item("апельсины", 80)
store1.add_item("виноград", 250)

store2 = Store("Фруктовый Рай", "Бульвар Роз, 12")
store2.add_item("яблоки", 50)
store2.add_item("апельсины", 80)
store2.add_item("виноград", 250)
store2.add_item("морковь", 25)
store2.add_item("картофель", 20)
store2.add_item("огурцы", 15)

store3 = Store("Овощная Лавка", "Проезд Зеленый, 3")
store3.add_item("яблоки", 50)
store3.add_item("морковь", 25)
store3.add_item("картофель", 20)
store3.add_item("огурцы", 15)

# Использование методов класса для работы с товарами
store1.update_price, store2.update_price, store3.update_price("аперелисины", 60)  # Обновление цены на яблоки
print(f"Цена яблок в магазине '{store1.name}',{store2.name},{store3.name}': {store1.get_price('яблоки')}, {store2.get_price('яблоки')}, {store3.get_price('яблоки')}")
store2.remove_item("grapes")  # Удаление товара
print(f"Цена винограда в магазине '{store2.name}': {store2.get_price('виноград')}")
store3.get_price("морковь")
print(f"Цена моркови в магазине '{store3.name}': {store3.get_price('морковь')}")


