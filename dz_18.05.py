
class Fooditem:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price
    def __str__(self):
        return f'Name: {self.name}, Description: {self.description}, Price: {self.price}'
class Menu:
    def __init__(self):
        self.menu_list = []
    def add_to_menu(self, food):
        self.menu_list.append(food)
        print(f'\nСтрава "{food.name}" була додана у Меню')
    def remove_from_menu(self, food):
        if food in self.menu_list:
            self.menu_list.remove(food)
            print(f'\nСтрава "{food.name}" була видалена з Меню')
        else:
            print(f'\nСтрава "{food.name}" не знайдена у Меню')
    def __str__(self):
        return '\n'.join([str(food) for food in self.menu_list])

food_0 = Fooditem('Салат Цезар', 'Салат із томатів, зелені та сиру Фета', 120)
food_1 = Fooditem('Сирна тарілка', 'Тарілка із сирами: Пармезаном, Брі, Чедер та Французький', 160 )
food_2 = Fooditem("Стейк Гов'яжий", "Гов'яжий стейк, маринований у фірмовому соусі", 125)
food_3 = Fooditem('Чай холодний', 'Холодний чорний чай із лимоном', 65)
food_4 = Fooditem('Піца', 'Піца Маргарита із томатами, соусом та базиліком', 150)
menu = Menu()
menu.menu_list = [food_0, food_1, food_2, food_3]

print(menu)

menu.remove_from_menu(food_0)
menu.add_to_menu(food_4)

class Order:
    def __init__(self):
        self.order_list = []
    def add_item(self, food):
        self.order_list.append(food)
        print(f'\nСтрава "{food.name}" була додана до Замовлення')
    def remove_item(self, food):
        if food in self.order_list:
            self.order_list.remove(food)
            print(f'\nСтрава "{food.name}" була видалена з Замовлення')
        else:
            print(f'\nСтрава "{food.name}" не була знайдена в Замовленні')
    def __str__(self):
        bill = 0
        for food in self.order_list:
            bill += food.price
        print(f'\nЧек: {bill}грн')
        return '\n'.join([str(food) for food in self.order_list])

class Restaurant(Order, Menu):
    def __init__(self):
        super().__init__()
        self.menu = Menu()
        self.order = Order()
    def add_food_item_to_menu(self, food):
        self.menu.add_to_menu(food)
    def remove_food_item_from_menu(self, food):
        self.menu.remove_from_menu(food)
    def add_to_order(self, food):
        self.order.add_item(food)
    def remove_from_order(self, food):
        self.order.remove_item(food)

restaurant = Restaurant()

order = Order()
order.order_list = [food_2, food_3, food_4]
order.remove_item(food_3)

restaurant.order.add_item(food_1)

print(order)

with open('Bill.txt', 'w') as file:
    file.write(str(order))