#5
class Department:
    def __init__(self, name="ChE Department", section=5):
        self.name = name
        self.sec = section
        self.avr = 0
        self.total = 0
        print(f"The {self.name} has {section} sections.")

    def add_students(self, *num):
        if self.sec == len(num):
            self.total = sum(list(num))
            self.avr = round(self.total / self.sec, 2)

    def merge_Department(self, *depts):
        mega_total = self.avr * self.sec
        mega_sec = self.sec
        for dept in depts:
            mega_total += dept.avr * dept.sec
            print(f"{dept.name} is merged to Engineering Department.")
        mega = mega_total / (mega_sec + sum(dept.sec for dept in depts))
        print(f"Now the {self.name} has an average of {mega:.2f} students in each section.")


d1 = Department()
print('1-----------------------------------')
d2 = Department('MME Department')
print('2-----------------------------------')
d3 = Department('NCE Department', 8)
print('3-----------------------------------')
d1.add_students(12, 23, 12, 34, 21)
print('4-----------------------------------')
d2.add_students(40, 30, 21)
print('5-----------------------------------')
d3.add_students(12, 34, 41, 17, 30, 22, 32, 51)
print('6-----------------------------------')
mega = Department('Engineering Department', 10)
print('7-----------------------------------')
mega.add_students(21, 30, 40, 36, 10, 32, 27, 51, 45, 15)
print('8-----------------------------------')
print(mega.merge_Department(d1, d2))
print('9-----------------------------------')
print(mega.merge_Department(d3))
