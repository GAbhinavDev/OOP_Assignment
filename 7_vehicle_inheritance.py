class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")


class Car(Vehicle):
    def __init__(self, brand, model, seats):
        super().__init__(brand, model)
        self.seats = seats

    def display_info(self):
        super().display_info()
        print(f"Type: Car, Seats: {self.seats}")


class Bike(Vehicle):
    def __init__(self, brand, model, cc):
        super().__init__(brand, model)
        self.cc = cc

    def display_info(self):
        super().display_info()
        print(f"Type: Bike, Engine CC: {self.cc}")


# Example usage
if __name__ == "__main__":
    car = Car("Toyota", "Camry", 5)
    bike = Bike("Yamaha", "R15", 155)

    car.display_info()
    print()
    bike.display_info()