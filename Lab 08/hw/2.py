#2
class Exam:
    def __init__(self,marks):
        self.marks = marks
        self.time = 60
        
    def examSyllabus(self):
        return "Maths , English"
    def examParts(self):
        return "Part 1 - Maths\nPart 2 - English\n"
    
class ScienceExam(Exam):
    def __init__(self, marks, time, *subjects):
        super().__init__(marks)
        self.time = time
        self.subs = subjects

    def __str__(self):
        return f"Marks: {self.marks} Time: {self.time} Number of Parts: {2 + len(self.subs)}"

    def examSyllabus(self):
        return super().examSyllabus() + ' , ' + ' , '.join(sub for sub in self.subs)
    
    def examParts(self):
        # self.parts = []
        # for i in range(len(self.subs)):
        #     self.parts.append(f"Part {i+3} - {self.subs[i]}")
        # return super().examParts() + '\n'.join(self.parts)

        return super().examParts() + '\n'.join([(f"Part {i+3} - {self.subs[i]}") for i in range(len(self.subs))])
engineering = ScienceExam(100,90,"Physics","HigherMaths")
print(engineering)
print('----------------------------------')
print(engineering.examSyllabus())
print(engineering.examParts())
print('==================================') 
architecture = ScienceExam(100,120,"Physics","HigherMaths","Drawing")
print(architecture)
print('----------------------------------')
print(architecture.examSyllabus())
print(architecture.examParts())