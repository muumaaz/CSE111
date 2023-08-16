#2
class MangoTree:
    def __init__(self, variety, height = 1.0, number_of_mangoes = 0):
        self.variety = variety
        self.height = height
        self.number_of_mangoes = number_of_mangoes

mangoTree1= MangoTree("Gopalbhog")
# Display the details of the mango tree
print("=====================================")
print("Mango Tree Details:")
print(f"Variety: {mangoTree1.variety}")
print(f"Height: {mangoTree1.height} meter(s)")
print(f"Number of mangoes on the tree: {mangoTree1.number_of_mangoes}")
print("=====================================")
mangoTree2= MangoTree("Amrapali")
# Display the details of the mango tree
print("Mango Tree Details:")
print(f"Variety: {mangoTree2.variety}")
print(f"Height: {mangoTree2.height} meter(s)")
print(f"Number of mangoes on the tree: {mangoTree2.number_of_mangoes}")
print("=====================================")

print("Updated details after 5 years:")
print("=====================================")
mangoTree1.height = round(5*3 + mangoTree1.height)
mangoTree1.number_of_mangoes = mangoTree1.height * 10

mangoTree2.height = round(5*3 + mangoTree2.height)
mangoTree2.number_of_mangoes = mangoTree2.height * 15

print(f"Variety: {mangoTree1.variety}")
print(f"Height: {mangoTree1.height} meter(s)")
print(f"Number of mangoes on the tree: {mangoTree1.number_of_mangoes}")
print("=====================================")
print(f"Variety: {mangoTree2.variety}")
print(f"Height: {mangoTree2.height} meter(s)")
print(f"Number of mangoes on the tree: {mangoTree2.number_of_mangoes}")
print("=====================================")

