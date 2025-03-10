class Student:
    def __init__(self, student_id, name, age):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.courses = []
        self.grades = {}

    def enroll_in_class(self, course_id):
        if course_id not in self.courses:
            self.courses.append(course_id)

    def list_classes(self):
        return self.courses

    def add_grade(self, course_id, grade):
        if course_id in self.grades:
            self.grades[course_id].append(grade)
        else:
            self.grades[course_id] = []
            self.grades[course_id].append(grade)

    def get_average_grade(self):
        for course_id, value in self.grades.items():
            print(course_id, sum(value) / len(value))


class Class:
    def __init__(self, class_id, name, instructor):
        self.class_id = class_id
        self.name = name
        self.instructor = instructor
        self.students = {}

    def add_student(self, student_id):
        if student_id not in self.students:
            self.students[student_id] = []

    def list_students(self):
        for student_id in self.students.keys():
            print(student_id)

    def add_grade(self, student_id, grade):
        if student_id in self.students:
            self.students[student_id].append(grade)
        else:
            self.students[student_id] = []
            self.students[student_id].append(grade)

    def get_average_grade(self):
        counter = 0
        sum = 0
        for grades in self.students.keys():
            counter += 1
            sum += sum(grades) / len(grades)

        return sum / counter


class SalymbekovUniversity:
    def __init__(self):
        self.students = {}
        self.classes = {}

    def add_student(self, student):
        if student.student_id not in self.students:
            self.students[student.student_id] = student
            print("Student added: ", student.name)
        else:
            print("Student already exists")

    def add_class(self, university_class):
        if university_class.class_id not in self.classes:
            self.classes[university_class.class_id] = university_class
            print("Class added")
        else:
            print("Class already exists")

    def enroll_student(self, student_id, class_id):
        if student_id in self.students and class_id in self.classes:
            self.classes[class_id].add_student(student_id)
            self.students[student_id].enroll_in_class(class_id)
            print(
                "Student enrolled in class:",
                self.students[student_id].name,
                self.classes[class_id].name,
            )
        else:
            print("Student or class does not exist")

    def search_student(self, student_id):
        if student_id in self.students:
            return self.students[student_id]
        else:
            print("Student does not exist")

    def search_class(self, class_id):
        if class_id in self.classes:
            return self.classes[class_id]
        else:
            print("Class does not exist")

    def update_student(self, student_id, new_data):
        if student_id in self.students:
            self.students[student_id] = new_data
            print("Student updated")
        else:
            print("Student does not exist")

    def update_class(self, class_id, new_data):
        if class_id in self.classes:
            self.classes[class_id] = new_data
            print("Class updated")
        else:
            print("Class does not exist")

    def total_students(self):
        return len(self.students)

    def total_classes(self):
        return len(self.classes)

    def students_in_class(self, class_id):
        return self.classes[class_id].list_students()

    def classes_for_student(self, student_id):
        return self.students[student_id].list_classes()

    def average_grade_for_student(self, student_id):
        return self.students[student_id].get_average_grade()

    def average_grade_for_class(self, class_id):
        return self.classes[class_id].get_average_grade()

    def add_grade(self, student_id, class_id, grade):
        if class_id in self.classes and student_id in self.students:
            self.classes[class_id].add_grade(student_id, grade)
            self.students[student_id].add_grade(class_id, grade)
            print("Added grade to student", student_id)


university = SalymbekovUniversity()

student1 = Student(1234, "Elnura", 20)
student2 = Student(2, "Aibek", 20)

university.add_student(student1)
university.add_student(student2)

class2 = Class(2, "Math", "John")

university.add_class(Class(1, "Math", "John"))
university.add_class(class2)

university.enroll_student(1234, 1)
university.enroll_student(2, 2)

university.add_grade(1, 1234, 24)

student1.add_grade(1, 23)
