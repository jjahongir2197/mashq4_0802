class Lesson:
    def __init__(self, title):
        self.title = title


class Course:
    def __init__(self, name):
        self.name = name
        self.lessons = []

    def add_lesson(self, l):
        self.lessons.append(l)


class Student:
    def __init__(self, name):
        self.name = name
        self.progress = {}

    def enroll(self, course):
        self.progress[course.name] = 0

    def study(self, course):
        if self.progress[course.name] < len(course.lessons):
            self.progress[course.name] += 1

    def report(self):
        for c, p in self.progress.items():
            print(c, ":", p, "dars")


python_course = Course("Python")
for i in range(10):
    python_course.add_lesson(Lesson(f"Dars {i+1}"))

s = Student("Jahongir")
s.enroll(python_course)

for _ in range(4):
    s.study(python_course)

s.report()

