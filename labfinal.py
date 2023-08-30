class Instructor:
    instructor_database={}
    no_of_STs=0
    no_of_teachers=0
    no_of_students_taught=0
    def __init__(self, name,no_of_students_taught,*courses_taught):
        self.name = name
        self.role = 'Instructor'
        self.no_of_students_taught=no_of_students_taught
        self.courses_taught=list(courses_taught)
    def instruct(self):
        print(f"I am helping {self.no_of_students_taught} students with their studies")

    def details(self):
        return "Name:{}\nRole:{}\nNo.of students taught:{}\nCourses taught:{}".format(self.name,self.role, self.no_of_students_taught,self.courses_taught)
#Write your code here

class StudentTutor(Instructor):
    def __init__(self, name, no_of_students_taught, stid, com_cred, id, *courses):
        super().__init__(name, no_of_students_taught, *courses)
        self.role = "Student Tutor"
        self.stid = stid
        self.com_cred = com_cred
        self.id = id
        Instructor.no_of_STs += 1
        Instructor.instructor_database[f"ST{Instructor.no_of_STs}"] = {'No_of_students_taught' : f"{Instructor.no_of_students_taught}", 'Courses_taught' : len(self.courses_taught)}
        

    def instruct(self):
        print(f"I am assisting {self.no_of_students_taught} students in {len(self.courses_taught)} course(s)")


    def details(self):
        return f"Name: {self.name} \nRole: {self.role} \nNo. of students taught: {self.no_of_students_taught} \nST ID: {self.stid} \nStudent ID: {self.id} \nCredits Completed: {self.com_cred} \nCourses taught:{self.courses_taught}"

    def attend_lectures(self):
        print(f"I have already completed {self.com_cred} credits. I am attending lectures to complete my degree.")

class Teacher(Instructor):
    def __init__(self, name, no_of_students_taught, chair, *courses):
        super().__init__(name, no_of_students_taught, *courses)
        self.role = "Teacher"
        self.designation = chair
        Instructor.no_of_teachers += 1
        Instructor.instructor_database[f"T{Instructor.no_of_teachers}"] = {'No_of_students_taught' : f"{Instructor.no_of_students_taught}", 'Courses_taught' : len(self.courses_taught)}
        

    def instruct(self):
        print(f"I am teaching {len(self.courses_taught)} course(s) to {self.no_of_students_taught} students")

    def details(self):
        return f"Name: {self.name} \nRole: {self.role} \nNo. of students taught: {self.no_of_students_taught} \nDesignation: {self.designation} \nCourses taught:{self.courses_taught}"


    def check_copies(self):
        print(f"Checking copies of {self.no_of_students_taught} students")    



Instructor1 = Instructor("Habib",50,"CSE 110", "CSE 111")
Instructor1.instruct()
print("---------------------------")
print(Instructor1.details())
print("---------------------------")
ST1 = StudentTutor("Nazifa",80,"T46",80,21230896,"CSE 111","CSE 220")
ST1.instruct()
print("---------------------------")
print(ST1.details())
print("---------------------------")
ST1.attend_lectures()
print("---------------------------")
print("Instructor database:", Instructor.instructor_database)
print("---------------------------")
Teacher1 = Teacher("Salma",200,"Lecturer","CSE 110", "CSE 111","CSE221")
Teacher1.instruct()
print("---------------------------")
print(Teacher1.details())
print("---------------------------")
Teacher1.check_copies()
print("---------------------------")
Teacher2 = Teacher("Ramisa",120,"Assistant Professor","CSE 470")
Teacher2.instruct()
print("---------------------------")
print(Teacher2.details())
print("---------------------------")
Teacher2.check_copies()
print("---------------------------")
ST2 = StudentTutor("Hannan",120,"T49",80,21200987, "CSE 110", "CSE 111","CSE 220")
ST2.instruct()
print("---------------------------")
print(ST2.details())
print("---------------------------")
ST2.attend_lectures()
print("---------------------------")
print("Instructor database:", Instructor.instructor_database)
print("---------------------------")