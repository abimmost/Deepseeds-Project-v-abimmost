# CREATING A CLASS
# ThisRIghtHereIsCalled Pascal casing
class Student:
    # A constructor is needed for the class
    def __init__(self, name, matricule, gpa, gender):  # 'self' is a default empty object
        self.name = name
        self.matricule = matricule
        self.gpa = gpa
        self.gender = gender
        pass

    # Behaviours/functions
    def register(self):
        return f"{self.name} is having matricule {self.matricule}"
    def take_lesson(self):
        return f"{self.name} with matricule {self.matricule} registered Geology"
    def drop_lesson(self):
        return f"{self.name} with matricule {self.gpa} dropped Geology"
    # pass

first_student = Student("Allen", "UBa23PB162", 1.99, "Him")
second_student = Student("Nita", "UBa23PB025", 2.0, "Male")

print(f"First Student:\n{first_student.name}, {first_student.matricule}, {first_student.gpa}, {first_student.gender}")

print(f"First Student {first_student.name} is Taking Lesson {first_student.drop_lesson}")