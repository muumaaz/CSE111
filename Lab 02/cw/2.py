#2
def panda(food, place = "Mohakhali"):
    menu = {"BBQ Chicken Cheese Burger": 250,
            "Beef Burger": 170,
            "Naga Drums" : 200
    }
    if place == "Mohakhali":
        delivery_charge = 40
    else:
        delivery_charge = 60

    price = round(menu[food] + (menu[food] * 8 / 100), 1)

    total = price + delivery_charge

    return total

usr = input().split(', ')
food = usr[0]
if len(usr) > 1:
    place = usr[1]

price = panda(food, place)
print(price)