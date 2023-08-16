#3
class Student:
    def __init__(self, name, cg, credit = 9, dept = "CSE"):
        self.name = name
        self.cg = cg
        self.credit = credit
        self.dept = dept

    def checkScholarshipEligibility(self):
        if self.credit > 10 and self.cg >= 3.5:
            self.scholarship_status = ''
            if self.cg > 3.7:
                self.scholarship_status = "Merit-based scholarship"
            else:
                self.scholarship_status = "Need-based scholarship"
            print(f"{self.name} is eligible for {self.scholarship_status}.")
        else:
            self.scholarship_status = "No scholarship "
            print(f"{self.name} is not eligible for scholarship.")

    def showDetails(self):
        print(f"Name: {self.name}")
        print(f"Department: {self.dept}")
        print(f"CGPA: {self.cg}")
        print(f"Number of Credit: {self.credit}")
        print(f"Scholarship Status: {self.scholarship_status}")

print('--------------------------')
std1 = Student("Alif",3.99,12)
print('--------------------------')
std1.checkScholarshipEligibility()
print('--------------------------')
std1.showDetails()
print('--------------------------')
std2 = Student("Mim",3.4)
std3 = Student("Henry",3.5,15,"BBA")
print('--------------------------')
std2.checkScholarshipEligibility()
print('--------------------------')
std3.checkScholarshipEligibility()
print('--------------------------')
std2.showDetails()
print('--------------------------')
std3.showDetails()
print('--------------------------')
std4 = Student("Bob",4,6,"CSE")
print('--------------------------')
std4.checkScholarshipEligibility()
print('--------------------------')
std4.showDetails()

