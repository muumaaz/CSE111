#3
class Contacts:
    def __init__(self, names, numbers):
        self.contactDict = {}
        if len(names) != len(numbers):
            print("Contacts cannot be saved. Length Mismatch!")
        else:
            for i in range(len(names)):
                self.contactDict[names[i]] = numbers[i]

names = ["Emergency", "Father", "Bestie"]
numbers = ["999", "01xx23", "01xx87", "01xx65", "01xx43"]

m1 = Contacts(names, numbers)
print("Saved Contacts:", m1.contactDict)
print("---------------------------------------------")

names.append("Mother")
numbers.pop()

m2 = Contacts(names, numbers)
print("Saved Contacts:", m2.contactDict)

temp = m1

m1 = Contacts(names, numbers)

print(f"first m1: {temp}")
print("Second m1:", m1)