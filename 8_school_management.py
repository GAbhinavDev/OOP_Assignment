from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, role):
        self.name = name
        self.role = role

    @abstractmethod
    def get_details(self):
        pass


class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name, "Student")
        self.grade = grade

    def get_details(self):
        print(f"{self.role} - Name: {self.name}, Grade: {self.grade}")


class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name, "Teacher")
        self.subject = subject

    def get_details(self):
        print(f"{self.role} - Name: {self.name}, Subject: {self.subject}")


# Example usage
if __name__ == "__main__":
    s = Student("Abhinav", "10th")
    t = Teacher("Swathi", "Mathematics")

    s.get_details()
    t.get_details()