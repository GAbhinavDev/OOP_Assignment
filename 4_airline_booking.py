class Passenger:
    def __init__(self, name, passport_no):
        self.name = name
        self.passport_no = passport_no

    def display_info(self):
        print(f"Passenger Name: {self.name}, Passport No: {self.passport_no}")


class Booking(Passenger):
    def __init__(self, name, passport_no, flight_no):
        super().__init__(name, passport_no)
        self.flight_no = flight_no
        self.is_booked = False

    def book_ticket(self):
        self.is_booked = True
        print(f"Ticket booked on flight {self.flight_no} for {self.name}")

    def cancel_ticket(self):
        if self.is_booked:
            self.is_booked = False
            print(f"Ticket cancelled for {self.name}")
        else:
            print("No ticket to cancel")

    def display_status(self):
        status = "Booked" if self.is_booked else "Not Booked"
        print(f"{self.name}'s booking status: {status}")


# Example usage
if __name__ == "__main__":
    p1 = Booking("Abhinav", "A1234567", "AI2025")
    p1.display_info()
    p1.display_status()
    p1.book_ticket()
    p1.display_status()
    p1.cancel_ticket()
    p1.display_status()