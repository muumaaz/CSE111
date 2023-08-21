class KK_tea:
    sales_log = {}

    def __init__(self, price = 250, bags = 50):
        self.flavour = "KK Regular Tea"
        self.bags = bags
        self.price = price
        self.weight = self.bags * 2
        self.status = False
       

    def product_detail(self):
        print(f"Name: {self.flavour}, Weight: {self.weight}")
        print(f"Tea Bags: {self.bags}, Price: {self.price}")
        print(f"Status: {self.status}")

    @classmethod
    def total_sales(cls):
        print(cls.sales_log)

    @classmethod
    def update_sold_status_regular(cls, *teas):
        for tea in teas:
            tea.status = True
            cls.sales_log[tea.flavour] = cls.sales_log.get(tea.flavour, 0) + 1

class KK_flavoured_tea(KK_tea):
    def __init__(self, flavour, price, bags):
        super().__init__(price, bags)
        self.flavour = f"KK {flavour} Tea"

    @classmethod
    def update_sold_status_flavoured(cls, *teas):
        for tea in teas:
            tea.status = True
            cls.sales_log[tea.flavour] = cls.sales_log.get(tea.flavour, 0) + 1


t1 = KK_tea(250)
print("-----------------1-----------------")
t1.product_detail()
print("-----------------2-----------------")
KK_tea.total_sales()
print("-----------------3-----------------")
t2 = KK_tea(470, 100)
t3 = KK_tea(360, 75)
KK_tea.update_sold_status_regular(t1, t2, t3)
print("-----------------4-----------------")
t3.product_detail()
print("-----------------5-----------------")
KK_tea.total_sales()
print("-----------------6-----------------")
t4 = KK_flavoured_tea("Jasmine", 260, 50)
t5 = KK_flavoured_tea("Honey Lemon", 270, 45)
t6 = KK_flavoured_tea("Honey Lemon", 270, 45)
print("-----------------7-----------------")
t4.product_detail()
print("-----------------8-----------------")
t6.product_detail()
print("-----------------9-----------------")
KK_flavoured_tea.update_sold_status_flavoured(t4, t5, t6)
print("-----------------10-----------------")
KK_tea.total_sales()
