class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def display_info(self):
        print(f"[User] Name: {self.name}, Email: {self.email}")


class Instructor(User):
    def __init__(self, name, email, subject):
        super().__init__(name, email)
        self.subject = subject

    def upload_content(self):
        print(f"Instructor {self.name} uploaded content for {self.subject}.")

    def display_info(self):
        print(f"[Instructor] Name: {self.name}, Email: {self.email}, Subject: {self.subject}")


class CourseCreator(Instructor):
    def __init__(self, name, email, subject, course_name):
        super().__init__(name, email, subject)
        self.course_name = course_name
        self.modules = []

    def create_course(self, modules):
        self.modules = modules
        print(f"Course '{self.course_name}' created with modules: {', '.join(modules)}")

    def display_info(self):
        print(f"[CourseCreator] Name: {self.name}, Email: {self.email}, Subject: {self.subject}, Course: {self.course_name}")


# Example usage
if __name__ == "__main__":
    user = User("Abhinav", "abhinav@example.com")
    instructor = Instructor("Swathi", "swathi@example.com", "Python Programming")
    creator = CourseCreator("Abhiram", "abhiram@example.com", "Web Dev", "Full Stack Bootcamp")

    user.display_info()
    instructor.display_info()
    instructor.upload_content()
    creator.display_info()
    creator.create_course(["HTML", "CSS", "JavaScript", "Backend"])