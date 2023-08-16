#3
# Write your class code here
class box:
    def __init__(self, cube):
        self.height = cube[0]
        self.width = cube[1]
        self.breadth = cube[2]

print("Box 1")
b1 = box([10,10,10])
print("=========================")
print("Height:", b1.height)
print("Width:", b1.width)
print("Breadth:", b1.breadth)
volume = b1.height * b1.width * b1.breadth
print(f"Volume of the box is {volume} cubic units.")
print("-------------------------")
print("Box 2")
b2 = box((30,10,10))
print("=========================")
print("Height:", b2.height)
print("Width:", b2.width)
print("Breadth:", b2.breadth)
volume = b2.height * b2.width * b2.breadth
print(f"Volume of the box is {volume} cubic units.")
b2.height = 300
print("Updating Box 2!")
print("Height:", b2.height)
print("Width:", b2.width)
print("Breadth:", b2.breadth)
volume = b2.height * b2.width * b2.breadth
print(f"Volume of the box is {volume} cubic units.")
print("-------------------------")
print("Box 3")
b3 = b2
print("Height:", b3.height)
print("Width:", b3.width)
print("Breadth:", b3.breadth)
volume = b3.height * b3.width * b3.breadth
print(f"Volume of the box is {volume} cubic units.")

one = (b3 == b2)
b3.width = 100
two = (b3 == b2)
print(one, two)
# What will be the values of the variables one and two? Explain your answer briefly in text.
# -> When b3 = b2 is executed, it means that b3 and b2 refer to the same object in memory.
# So one and two will be True because they are comparing the same object.
# What will be the value of b2.width? Has that value changed since the driver code ran?
# If yes, explain why in brief text.
# -> This value has changed since the driver code ran because b3 and b2 refer to the same object.
# When b3.width is assigned 100, it also affects the width attribute of the shared object,
# which is accessed through b2. Hence, the value of b2.width is updated to 100.