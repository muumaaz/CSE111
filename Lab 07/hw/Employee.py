import datetime

class Employee:
    #total_employee = 0
    employee_count = {"Programmer": 0, "HR": 0}

    def __init__(self, name, joining_date, work_experience, weekly_work_hour = 40):
        self.name = name
        self.year, self.month, self.day = joining_date.split("-")
        self.joining_date = f"{self.year}-{self.month}-{self.day}"
        self.work_experience = work_experience
        if weekly_work_hour > 60:
            print("Weekly work hour cannot be more than 60 hours")
            self.weekly_work_hour = 40
        elif weekly_work_hour < 40:
            print(f"{self.name} can not work for {weekly_work_hour} hours")
            self.weekly_work_hour = 40
        else:
            self.weekly_work_hour = weekly_work_hour

    @classmethod
    def showDetails(cls):
        print("Company Workforce:")
        total = cls.employee_count["Programmer"] + cls.employee_count["HR"]
        print(f"Total Employee/s: {total}")
        
        if cls.employee_count["Programmer"] > 0:
            print(f"Total Programmer/s: {cls.employee_count['Programmer']}")
        if cls.employee_count["HR"] > 0:
            print(f"Total HR Employee/s: {cls.employee_count['HR']}")


class Programmer(Employee):
    designation_list = [ "Junior Software Engineer", "Software Engineer", "Senior Software Engineer", "Technical Lead" ]
    base_salaries = { "Junior Software Engineer": 30000, "Software Engineer": 45000, "Senior Software Engineer": 70000, "Technical Lead": 120000}
    salary_increment = 15/100

    def __init__(self, name, joining_date, work_experience, weekly_work_hour=40):
        super().__init__(name, joining_date, work_experience, weekly_work_hour)
        super().employee_count["Programmer"] += 1
        #Employee.total_employee += 1
        self.id = self.createProgrammerId()
        self.designation = self.createDesignation()
        self.period = datetime.datetime.now().year - int(self.year)

    def showProgrammerDetails(self):
        print(f"Name: {self.name}")
        print(f"ID: {self.id}")
        print(f"Joining Date: {self.day}-{self.month}-{self.year}")
        print(f"Work Experience: {self.work_experience}")
        print(f"Designation: {self.designation}")
        print(f"Salary: {round(self.salary, 1)}")

    def calculateSalary(self):
        self.salary = Programmer.base_salaries[self.designation] * (1 + Programmer.salary_increment)**self.period
        return round(self.salary, 1)
    
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

    def calculateOvertime(self):
        if self.weekly_work_hour > 40:
            self.bonus = (self.weekly_work_hour - 40) * 4 * 500
            print(f"{self.name} will get BDT {self.bonus} overtime.")
            self.salary += self.bonus
        else:
            print(f"{self.name} will not get any overtime.")
            

class HR(Employee):
    def __init__(self, name, joining_date, work_experience, weekly_work_hour):
        super().__init__(name, joining_date, work_experience, weekly_work_hour)
        super().employee_count["HR"] += 1
        #Employee.total_employee += 1
        self.id = self.createHREmployeeID()

    def showHREmployeeDetails(self):
        print("HR Employee: ")
        print(f"Name: {self.name}")
        print(f"ID: {self.id}")
        print(f"Joining Date: {self.day}-{self.month}-{self.year}")
    
    def createHREmployeeID(self):
        return f"HR-{self.year}{self.month}-{self.employee_count['HR']}"

class InternProgrammer(Programmer):
    intern_count = 0

    def __init__(self, name, joining_date, intern_type = "Unpaid"):
        super().__init__(name, joining_date, work_experience = 0, weekly_work_hour = 40)
        Programmer.employee_count["Programmer"] -= 1
        InternProgrammer.intern_count += 1
        self.temp_id = self.createInternId()
        self.intern_type = intern_type
        self.status = self.checkStatus()

    
    def createInternId(self):
        return f"Temp_{InternProgrammer.intern_count}"

    def checkStatus(self):
        # months_in_company = datetime.datetime.now().year - int(self.year) * 12 + datetime.datetime.now().month - int(self.month)
        # if int(self.day) > 1:
        #     months_in_company -= 1
        # if months_in_company > 4:
        #     if int(self.month) in [1, 7]:
        #         status = "Eligible for promotion"
        #     else:
        #         status = "Not eligible for promotion"
        
        # return status
        if datetime.datetime.now().month - int(self.month) > 4 and int(self.month) in [1, 7]:
            return "Eligible for promotion"
        else:
            return "Not eligible for promotion"
        
    
    def showInternDetails(self):
        print("Intern (Programmer):")
        print(f"Name: {self.name}")
        print(f"ID: {self.temp_id}")
        print(f"Joining Date: {self.year}-{self.month}-{self.day}")
        print(f"Internship Type: {self.intern_type}")
        print(f"Status: {self.status}")

    def promoteToProgrammer(self):
        if self.status == "Eligible for promotion":
            InternProgrammer.intern_count -= 1
            print(f"{self.name} is promoted!")
            self.joining_date = datetime.datetime.now().strftime("%Y-%m-%d")
            return Programmer(self.name, self.joining_date, 0, 40)
        else:
            print(f"{self.name} cannot be promoted.")


Employee.showDetails()
print("=========1=========")
richard = Programmer("Richard Hendricks", "2021-06-08", 4, 48)
richard.calculateSalary()
print("=========2=========")
richard.showProgrammerDetails()
print("=========3=========")
richard.calculateOvertime()
print("=========4=========")
richard.showProgrammerDetails()
print("=========5=========")
monica = HR("Monica Hall", "2022-07-06", 2, 40)
print("=========6=========")
monica.showHREmployeeDetails()
print("=========7=========")
Employee.showDetails()
print("=========8=========")
gilfoyle = Programmer("Bertram Gilfoyle", "2020-03-02", 6, 35)
gilfoyle.calculateSalary()
print("=========9=========")
gilfoyle.calculateOvertime()
print("=========10=========")
gilfoyle.showProgrammerDetails()
print("=========11=========")
gavin = Programmer("Gavin Belson", "2016-12-20", 9)
gavin.calculateSalary()
gavin.calculateOvertime()
gavin.showProgrammerDetails()
Employee.showDetails()
print("=========12=========")
yang = InternProgrammer("Jian Yang", "2023-01-01")
yang.showInternDetails()
print("=========13=========")
jared = InternProgrammer("Jared Dunn", "2023-06-05", "Paid")
jared.showInternDetails()
print("=========14=========")
jared = jared.promoteToProgrammer()
print("=========15=========")
Employee.showDetails()
print("=========16=========")
yang = yang.promoteToProgrammer()
yang.calculateSalary()
yang.showProgrammerDetails()
print("=========17=========")
Employee.showDetails()