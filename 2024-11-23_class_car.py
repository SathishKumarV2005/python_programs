class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_details(self):
        print(f"Car Make: {self.make}, Model: {self.model}, Year: {self.year}")

# Creating an object for the car
car = Car("Tata Motors", "Safari", 1998)
car.display_details()
