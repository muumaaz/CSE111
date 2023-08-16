#4
class UniversalStudiosUser:
    def __init__(self, name, age, typ):
        self.name = name
        self.age = age
        self.typ = typ
        self.rides = {}
        self.total = 0
        print("Welcome to Universal Studios.")

    def selected_rides(self, *rides):
        for ride in rides:
            ride, price = ride.split('-')
            self.rides[ride] = int(price)
        print("Added ride(s) successfully.")


    def show_details(self):
        print("Your information:")
        print(f"Name: {self.name}, Age: {self.age}, Category: {self.typ}")
        print("Selected rides:")
        for key, value in self.rides.items():
            print(f"Ride: {key}, Amount: {value} dollar(s).")
            self.total += value

        if self.typ == "Special" and len(self.rides) > 3:
            self.total = self.total - (self.total * 20/100)

        print(f"Please pay {self.total} dollar(s).")



customer_1 = UniversalStudiosUser("Alice", 21, "Special")
print("--------- 1 ---------")
customer_1.selected_rides("Waterworld-100", "Accelerator-200", "DinoSoarin-50")
print("--------- 2 ---------")
customer_1.show_details()
print("=================")
customer_2 = UniversalStudiosUser("Bob", 20, "Normal")
print("--------- 3 ---------")
customer_2.selected_rides("Enchanted Airways-300", "Jurassic Park-500", "Accelerator-200", "DinoSoarin-50")
print("--------- 4 ---------")
customer_2.show_details()
print("=================")
customer_3 = UniversalStudiosUser("Mark", 15, "Special")
print("--------- 5 ---------")
customer_3.selected_rides("Transformers-450", "Jurassic Park-500", "Waterworld-100", "DinoSoarin-50")
print("--------- 6 ---------")
customer_3.show_details()
