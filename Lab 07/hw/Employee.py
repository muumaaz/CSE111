class Employee:
    employee_count = {"Programmer": 0, "HR": 0}

    def __init__(self, name, joining_date, work_experience, weekly_work_hour = 40):
        self.name = name
        self.year, self.month, self.day = joining_date.split("-")
        self.joining_date = f"{self.year}-{self.month}-{self.day}"
        self.work_experience = work_experience
        if weekly_work_hour > 60:
            print("Weekly work hour cannot be more than 60 hours")
            self.weekly_work_hour = weekly_work_hour

    @classmethod
    def showDetails(cls):
        total = 0
        for role in cls.employee_count:
            total += cls.employee_count[role]
        print("Company Workforce:")
        print(f"Total Employee/s: {total}")
        if cls.employee_count["Programmer"] > 0:
            print(f"Total Programmer/s: {cls.employee_count['Programmer']}")
        if cls.employee_count["HR"] > 0:
            print(f"Total HR Employee/s: {cls.employee_count['HR']}")

class Programmer(Employee):
    designation_list = [ "Junior Software Engineer", "Software Engineer", "Senior Software Engineer", "Technical Lead" ]

    def __init__(self, name, joining_date, work_experience, weekly_work_hour=40):
        super().__init__(name, joining_date, work_experience, weekly_work_hour)
        super().employee_count["Programmer"] += 1
        self.id = self.createProgrammerId()
        self.designation = self.createDesignation()
        

    def showProgrammerDetails(self):
        print(f"Name: {self.name}")
        print(f"ID: {self.id}")
        print(f"Joining Date: {self.day}-{self.month}-{self.year}")
        print(f"Work Experience: {self.work_experience}")
        print(f"Designation: {self.designation}")
        print(f"Salary: {self.calculateSalary()}")

    def calculateSalary(self):
        if self.designation == self.designation_list[0]:
            salary = 30000 * (1 + 15/100)**self.work_experience 
        elif self.designation == self.designation_list[1]:
            salary = 45000 * (1 + 15/100)**self.work_experience
        elif self.designation == self.designation_list[2]:
            salary = 70000 * (1 + 15/100)**self.work_experience
        else:
            salary = 120000 * (1 + 15/100)**self.work_experience
        return round(salary, 1)
    
    def calculateOverTime(self):
        if self.weekly_work_hour > 40:
            self.bonus = (self.weekly_work_hour - 40) * 4 * 500
            print(f"{self.name} will get BDT {self.bonus} overtime.")

    
    def createProgrammerId(self):
        return f"P-{self.year}{self.month}-{self.employee_count['Programmer']}"

    def createDesignation(self):
        if self.work_experience < 3:
            return self.designation_list[0]
        elif self.work_experience < 5:
            return self.designation_list[1]
        elif self.work_experience < 8:
            return self.designation_list[2]
        else:
            return self.designation_list[3]

    
            



Employee.showDetails()
print("=========1=========")
richard = Programmer("Richard Hendricks", "2021-06-08", 4, 48)
richard.calculateSalary()
print("=========2=========")
richard.showProgrammerDetails()
print("=========3=========")