class KK_tea:
    def __init__(self, bags = 50, price = 250):
        self.flavour = "Regular"
        self.bags = bags
        self.price = price
        self.weight = self.bags * 2
        self.status = False

    def product_detail(self):
        print(f"Name: KK {self.flavour} Tea, Weight: {self.weight}")
        print(f"Tea Bags: {self.bags}, Price: {self.price}")
        print(f"Status: {self.status}")







t1 = KK_tea(250)
print("-----------------1-----------------")
t1.product_detail()
print("-----------------2-----------------")
