#3
class Farmer:
    def __init__(self, name = None):
        self.name = name
        self.crops = []
        self.fishes = []
        if self.name == None:
            print("Welcome to your farm!")
        elif type(self.name) == str:
            print(f"Welcome to your farm, {self.name}")
        elif type(self.name) == int:
            print(f"Welcome to your farm. Your farm ID is {self.name}")

    def addCrops(self, *crops):
        self.crops.extend(list(crops))
        if len(crops) > 0:
            print(f"{len(crops)} crop(s) added.")
        else:
            print("No crop(s) added.")

    def addFishes(self, *fishes):
        self.fishes.extend(list(fishes))
        if len(fishes) > 0:
            print(f"{len(fishes)} fish(s) added.")
        else:
            print("No fish added.")

    def showGoods(self):
        if len(self.fishes) > 0:
            print(f"You have {len(self.fishes)} fish(s):")
            print(','.join(self.fishes))
        else:
            print("You don't have any fish(s).")

        if len(self.crops) > 0:
            print(f"You have {len(self.crops)} crop(s):")
            print(','.join(self.crops))
        else:
            print("You don't have any crop(s).")



f1 = Farmer()
print("-------------------")
f1.addCrops('Rice', "Jute", "Cinnamon")
print("-------------------")
f1.addFishes()
print("-------------------")
f1.addCrops('Mustard')
print("-------------------")
f1.showGoods()
print("-------------------")
f2 = Farmer("Korim Mia")
print("-------------------")
f2.addFishes('Pangash', 'Magur')
print("-------------------")
f2.addCrops("Wheat", "Potato")
print("-------------------")
f2.addFishes("Koi", "Tuna", "Sardine")
print("-------------------")
f2.showGoods()
print("-------------------")
f3 = Farmer(2865127000)
print("-------------------")
f3.addCrops()
print("-------------------")
f3.addFishes("Katla")
print("-------------------")
f3.showGoods()
print("-------------------")