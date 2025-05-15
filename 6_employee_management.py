class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def calculate_salary(self):
        return 0

    def display(self):
        print(f"Name: {self.name}, ID: {self.emp_id}, Salary: {self.calculate_salary()}")


class FullTimeEmployee(Employee):
    def __init__(self, name, emp_id, monthly_salary):
        super().__init__(name, emp_id)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary


class PartTimeEmployee(Employee):
    def __init__(self, name, emp_id, hourly_rate, hours_worked):
        super().__init__(name, emp_id)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked


# Example usage
if __name__ == "__main__":
    e1 = FullTimeEmployee("Abhinav", "FT101", 50000)
    e2 = PartTimeEmployee("Swathi", "PT202", 500, 40)

    e1.display()
    e2.display()