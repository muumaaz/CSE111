#1
class NikeBangladesh:
    inventory = {"Air Jordan": 0, "Cortez": 0, "Zoom Kobe": 0}
    branches = []
    sold = 0

    def __init__(self, branch_name):
        self.branch_name = branch_name
        self.stock = {"Air Jordan": 0, "Cortez": 0, "Zoom Kobe": 0}
        self.sold = 0
        NikeBangladesh.branches.append(self.branch_name)

    @classmethod
    def status(cls):
        print("Nike Bangladesh Status:")
        print(f"Branches Opened: {cls.branches}")
        print(f"Currently Stocked")
        print(f"{cls.inventory}")

    def details(self):
        print(f"Nike {self.branch_name} outlet:")
        print(f"Product currently stocked:")
        print(f"{self.stock}")
        print(f"Sold: {self.sold}")

    def restockProducts(self, lots):
        for product, quantity in lots.items():
            if product in self.stock:
                self.stock[product] += quantity
                NikeBangladesh.inventory[product] += quantity

    def productSold(self, sells):
        for product, quantity in sells.items():
            if product in self.stock:
                self.stock[product] -= quantity
                NikeBangladesh.inventory[product] -= quantity


print("xxxxxxxxxxxxxx1xxxxxxxxxxxxxxxx")
NikeBangladesh.status()
dhaka = NikeBangladesh("Dhaka Banani")
chittagong = NikeBangladesh("Chittagong GEC")
print("xxxxxxxxxxxxxx2xxxxxxxxxxxxxxxx")
dhaka.details()
print("xxxxxxxxxxxxxx3xxxxxxxxxxxxxxxx")
chittagong.details()
print("xxxxxxxxxxxxxx4xxxxxxxxxxxxxxxx")
dhaka.restockProducts(
{"Air Jordan":1200,"Cortez":200,"Zoom Kobe":200})
chittagong.restockProducts(
{"Air Jordan":1000,"Cortez":250,"Zoom Kobe":100})
print("xxxxxxxxxxxxxx5xxxxxxxxxxxxxxxx")
NikeBangladesh.status()
print("xxxxxxxxxxxxxx6xxxxxxxxxxxxxxxx")
dhaka.productSold({"Air Jordan":760,"Cortez":90})
chittagong.productSold({"Air Jordan":520,"Zoom Kobe":70})
print("xxxxxxxxxxxxxx7xxxxxxxxxxxxxxxx")
NikeBangladesh.status()