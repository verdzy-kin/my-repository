class Student:
    def __init__(self, name, matricule, gpa, gender):
        self.name = name
        self.matricule = matricule
        self.gpa = gpa
        self.gender = gender
    def takeCourse(self):
        return f"{self.name} has matricule {self.matricule}"
    def dropCourse(self):
        return f"{self.name} is dropping linear algebra"

firstStudent = Student("Delsy", "UBa24Ph097", 3.35, "Female")
secondStudent = Student("Nita", "UBa23S1457", 3.41, "Female")
thirdStudent = Student("Mbom", "UBa20PB189", 2.95, "Male")
fourthStudent = Student("Clary", "UBa24Ph097", 1.09, "Female")


print(f" First student's name is: {firstStudent.name}\n First student's matricule is: {firstStudent.matricule}\n First student's GPA is: {firstStudent.gpa}\n First student's gender is: {firstStudent.gender}\n")
print(f"taking lesson: {firstStudent.takeCourse()}")