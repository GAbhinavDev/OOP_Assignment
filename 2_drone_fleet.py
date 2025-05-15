class Device:
    def __init__(self, device_id, model):
        self.device_id = device_id
        self.model = model

    def device_info(self):
        print(f"Device ID: {self.device_id}, Model: {self.model}")

class Flyer:
    def fly(self):
        print("Drone is flying...")

class Drone(Device, Flyer):
    def __init__(self, device_id, model):
        Device.__init__(self, device_id, model)

    def capture_image(self):
        print("Image captured by drone.")

# Example usage
drone1 = Drone("DR001", "X5C Syma")
drone1.device_info()
drone1.fly()
drone1.capture_image()