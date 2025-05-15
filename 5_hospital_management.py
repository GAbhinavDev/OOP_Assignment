class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Patient(Person):
    def __init__(self, name, age, patient_id):
        super().__init__(name, age)
        self.patient_id = patient_id
        self.diagnosis = None

    def admit(self, diagnosis):
        self.diagnosis = diagnosis
        print(f"Patient {self.name} admitted with diagnosis: {self.diagnosis}")

    def discharge(self):
        print(f"Patient {self.name} discharged.")
        self.diagnosis = None

    def display_status(self):
        status = f"Diagnosis: {self.diagnosis}" if self.diagnosis else "Not admitted"
        print(f"Patient {self.name} ({self.patient_id}) - {status}")


# Example usage
if __name__ == "__main__":
    patient1 = Patient("Abhinav", 22, "P1001")
    patient1.display_info()
    patient1.display_status()
    patient1.admit("Fever and Cold")
    patient1.display_status()
    patient1.discharge()
    patient1.display_status()