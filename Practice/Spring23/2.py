class ChefsCounter:
    reservation = {}

    def __init__(self, location, table = 5):
        self.location = location
        self.table = table
        self.person = []
        print(f"The {self.location} banch of Chef's Counter is open for reservation!")

    def reserve(self, *persons):
        for person in persons:
            if len(self.person) < self.table:
                self.person.append(person)
            else:
                print(f"Sorry, {person}, {self.table} people already made a resevation in this branch.")
        ChefsCounter.reservation[self.location] = self.person

    def reservation_info(self):
        print(f"Customers who reserved in Gulshan branch:")
        print(', '.join(self.person))

    @classmethod
    def createNewBranch(cls, location, table = 5):
        return cls(location, table)
        

print("===============1=============")
branch1 = ChefsCounter("Gulshan")
branch1.reserve("Sam", "Paul")
print("===============3=============")
branch1.reservation_info()
print("===============4=============")
branch1.reserve("John", "Robin", "Billy", "Robert")
print("===============5=============")
branch1.reservation_info()
print("===============6=============")
branch2 = ChefsCounter("Dhanmondi",7)
branch2.reserve("Ben", "Alice", "Fred")
print("===============8=============")
branch2.reservation_info()
print("===============9=============")
branch2.reserve("Tom", "Ken", "Garet", "Miles", "Taylor")
print("===============10=============")
branch2.reservation_info()
print("===============11=============")
branch3 = ChefsCounter.createNewBranch("100 feet")
print("===============12=============")
branch3.reserve("Harry", "Bob", "Jenny")
print("===============13=============")
branch3.reservation_info()
print("===============14=============")
print("Reservation Information of All Branches:", ChefsCounter.reservation)