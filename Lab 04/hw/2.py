#2
class Foodie:
    def __init__(self, name):
        self.name = name
        self.total = 0
        self.items = []
        self.cart = []

    def order(self, *items):
        self.items = items
        for item in self.items:
            food, quantity = item.split('-')
            price = menu[food]
            total_price = int(quantity) * price
            print(f"Ordered - {food}, quantity - {quantity}, price(per unit) - {price}")
            print(f"Total price - {total_price}")
            self.total += total_price
            self.cart.append(food)

    def show_orders(self):
        return f"{self.name} has {len(self.items)} items in the cart \nItems: {list(self.cart)} \nTotal spent: {self.total}"

    def pay_tips(self, tip = None):
        if tip == None:
            print("No tips to the waiter.")
        else:
            print(f"Gives {tip}/- tips to the waiter")
            self.total += tip

menu = {'Chicken Lollipop':15,'Beef Nugget':20,'Americano':180,'Red Velvet':150,'Prawn Tempura':80,'Saute Veg':200}

f1 = Foodie('Frodo')
print(f1.show_orders())
print('1----------------------')
f1.order('Chicken Lollipop-3','Beef Nugget-6','Americano-1')
print('2----------------------')
print(f1.show_orders())
print('3----------------------')
f1.order('Red Velvet-1')
print('4----------------------')
f1.pay_tips(20)
print('5----------------------')
print(f1.show_orders())
f2 = Foodie('Bilbo')
print('6----------------------')
f2.order('Prawn Tempura-6','Saute Veg-1')
print('7----------------------')
f2.pay_tips()
print('8----------------------')
print(f2.show_orders())

