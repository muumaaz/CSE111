#4
class Cakes:
    order_list = {}
    feedback_dic = {}

    def __init__(self, flavor, weight):
        self.flavor = flavor
        self.weight = weight
        self.sugar = 'Moderate sugar'
        self.cream = 'Whipped Cream'
        self.price = round((weight/1000) * 1200, 1)
        self.add_to_order_list()

    def add_to_order_list(self, cake = 'Cake'):
        if f"{self.flavor} {cake} {self.weight}gm" in Cakes.order_list:
            Cakes.order_list[f"{self.flavor} {cake} {self.weight}gm"] += 1
        else:
            Cakes.order_list[f"{self.flavor} {cake} {self.weight}gm"] = 1

    def cake_details(self):
        print(f"Flavor: {self.flavor} Cake, Weight: {self.weight} gm")
        print(f"Sweetness: {self.sugar}, Cream Type: {self.cream}")
        print(f"Price: {self.price}")

    def add_customization(self, sugar = None, cream = None):
        self.sugar = sugar
        self.cream = cream

    @classmethod
    def give_feedbacks(cls, cake, feedback):
        if cake in cls.feedback_dic:
            cls.feedback_dic[cake].append(feedback)
        else:
            cls.feedback_dic[cake] = [feedback]
        print("Thanks for your valuable feedback!")
    @classmethod
    def show_feedbacks(cls):
        print(cls.feedback_dic)

class Cheese_Cakes(Cakes):
    def __init__(self, flavor, weight, typ = 'Baked'):
        super().__init__(flavor, weight)
        self.price = round((weight/1000) * 1500, 1)
        self.cream = 'Cream Cheese'
        self.typ = typ
        self.add_to_order_list()
    
    def add_to_order_list(self):
        super().add_to_order_list("Cheese Cake")

    def cake_details(self):
        print(f"Flavor: {self.flavor} Cake, Weight: {self.weight} gm")
        print(f"Sweetness: {self.sugar}, Cream Type: {self.cream}")
        print(f"Cake Type: {self.typ}, Price: {self.price} Taka")

    def add_customization(self, sugar = None, cream = None):
        print("Sorry! No customization available for cheese cakes.")

    @classmethod
    def give_feedbacks(cls, cake, feedback):
        super().give_feedbacks(cake, feedback)
        print("You will get 10% discount for your next purchase!")

order_1=Cakes("Chocolate",500)
order_2=Cakes("Vanilla",800)
print("(1)**********************************")
order_1.cake_details()
print("(1.1)**********************************")
print(Cakes.order_list)
print("(2)**********************************")
order_2.add_customization("Zero","Butter Cream")
order_2.cake_details()
Cakes.give_feedbacks("Chocolate Cake","Very Delicious")
Cakes.give_feedbacks("Chocolate Cake","Yummy")
print("(4)**********************************")
Cakes.show_feedbacks()
print("(5)**********************************")
ch_order1=Cheese_Cakes("Red velvet",700)
ch_order1.cake_details()
print("(6)**********************************")
ch_order1.add_customization()
print("(7)**********************************")
ch_order2=Cheese_Cakes("Blue Berry",900,"No Bake")
ch_order2.cake_details()
print("(8)**********************************")
print(Cakes.order_list)
print("(9)**********************************")
Cheese_Cakes.give_feedbacks("Red velvet Cheese Cake","Average")
Cheese_Cakes.give_feedbacks("Blue Berry Cheese Cake","Liked it")
print("(10)**********************************")
Cakes.show_feedbacks()

