#Task 06
class StudentRoutineGenerator:
    def __init__(self, name, max_courses):
        self.name = name
        self.max_courses = max_courses
        self.schedule = {'Sat/Thurs': {}, 'Sun/Tue': {}, 'Mon/Wed': {}}
        self.current_courses = {}

    def addCourses(self, *args):
        for arg in args:
            course_name, day, time = arg.split('-')

            # check if the course is already in the schedule
            if course_name in self.current_courses:
                print(f'You already have {course_name} in your routine')
                continue

            # check if the time slot is free
            if time in self.schedule[day] and self.schedule[day][time] != course_name:
                print(f"Can't take {course_name}. It's clashing with your {self.schedule[day][time]}")
                continue

            # check if maximum number of courses has been reached
            if len(self.current_courses) >= self.max_courses:
                print(f"Can't take {course_name}. Maximum number of courses reached.")
                continue

            # add course to schedule
            self.schedule[day][time] = course_name
            self.current_courses[course_name] = (day, time)
            print(f'Successfully added {course_name}!')

    def dropCourse(self, course_name):
        # check if the course is in the schedule
        if course_name not in self.current_courses:
            print('No such course in your routine')
            return

        # remove course from schedule
        day, time = self.current_courses[course_name]
        del self.schedule[day][time]
        del self.current_courses[course_name]
        print(f'Successfully dropped {course_name}')

    def showRoutine(self):
        print('Updated Routine:')
        print(self.schedule)
        print('Routine Details:')
        for day, courses in self.schedule.items():
            print(day+':')
            for time, course in courses.items():
                print(time, '-', course)

print('##################################')
st1 = StudentRoutineGenerator('Harry', 4)
print('------------------------------')
st1.addCourses('CSE110-Mon/Wed-12:30', 'MAT110-Mon/Wed-2:00')
st1.addCourses('ENG101-Sun/Tue-12:30', 'CSE110-Mon/Wed-9:30')
st1.addCourses('PHY111-Sun/Tue-12:30')
print('------------------------------')
st1.showRoutine()
print('------------------------------')
st1.dropCourse('CSE110')
st1.dropCourse('PHY112')
print('------------------------------')
st1.showRoutine()
print('##################################')
st2 = StudentRoutineGenerator('John', 3)
print('------------------------------')
st2.addCourses('MAT110-Mon/Wed-8:00')
st2.addCourses('ENG101-Sat/Thurs-12:30', 'CSE110-Sun/Tue-9:30')
st2.addCourses('PHY111-Sun/Tue-12:30')
print('------------------------------')
st2.showRoutine()