#1
class Student:
    def __init__(self, name, id, cg):
        self.__name = name
        self.__id = id
        self.__cg = cg
    def getName(self):
        return self.__name

    def getId(self):
        return self.__id
    def setId(self, id):
        self.__id = id

    def getCg(self):
        return self.__cg

class Department:
    def __init__(self, dept):
        self.dept = dept
        self.students = []
        self.idlist = []

    def addStudent(self, *students):
        for student in students:
            if student.getId() not in self.idlist:
                self.idlist.append(student.getId())
                self.students.append((student))
                print(f"Welcome to {self.dept} department, {student.getName()}")
            else:
                print(f"Student with this ID already exists. Please try with another ID")

    def findStudent(self, id):
        if id in self.idlist:
            for student in self.students:
                if id == student.getId():
                    print("Student info:")
                    print(f"Student Name: {student.getName()}")
                    print(f"ID: {student.getId()}")
                    print(f"CGPA:  {student.getCg()}")
        else:
            print("Student with this ID doesn't exist, Please give a valid ID")


    def details(self):
        print(f"Department Name: {self.dept}")
        print(f"Number of student:{len(self.students)}")
        print(f"Details of the students: ")
        for student in self.students:
            print(f"Student name: {student.getName()}, ID: {student.getId()}, cgpa: {student.getCg()}")



s1 = Student("Akib", 22301010, 3.29)
s2 = Student("Reza", 22101010, 3.45)
s3 = Student("Ruhan", 23101934, 4.00)
print("1==================================")
cse = Department("CSE")
cse.findStudent(22112233)
#Student with this ID doesn't exist, Please give a valid ID
print("2==================================")
cse.addStudent(s1,s2,s3)
#Welcome to CSE department, Akib
#Welcome to CSE department, Reza
#Welcome to CSE department, Ruhan
print("3==================================")
cse.details()
print("4==================================")
cse.findStudent(22301010)
print("5==================================")
s4 = Student("Nakib",22301010,3.22)
cse.addStudent(s4)
print("6==================================")
s4.setId(21201220)
cse.addStudent(s4)
print("7==================================")
cse.details()
print("8==================================")
s5 = Student("Sakib",22201010,2.29)
cse.addStudent(s5)
print("9==================================")
cse.details()
