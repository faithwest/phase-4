import random
import string

def generate_number_plate(format="LLL###"):
    letters = string.ascii_uppercase
    numbers = string.digits

    plate = ""
    for char in format:
        if char == "L":
            plate += random.choice(letters)
        elif char == "#":
            plate += random.choice(numbers)
    return plate

# Example usage with a specific format
plate = generate_number_plate("XY#123")
print(plate)

import random
import string

class Car:
    def __init__(self, country_code, num_letters, num_digits):
        self.country_code = country_code
        self.num_letters = num_letters
        self.num_digits = num_digits
        self.number_plate = self.generate_number_plate()

    def generate_number_plate(self):
        # Generate random letters for the number plate
        letters = ''.join(random.choices(string.ascii_uppercase, k=self.num_letters))
        # Generate random digits for the number plate
        digits = ''.join(random.choices(string.digits, k=self.num_digits))
        # Concatenate country code, letters, and digits to form the number plate
        number_plate = self.country_code + ' ' + letters + ' ' + digits
        return number_plate

class CarTracker:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def track_cars(self):
        print("Tracking cars:")
        for car in self.cars:
            print("Car Number Plate:", car.number_plate)

def main():
    tracker = CarTracker()

    # Add some cars to the tracker
    num_cars = int(input("Enter the number of cars to track: "))
    for _ in range(num_cars):
        country_code = input("Enter the country code for the car: ")
        num_letters = int(input("Enter the number of letters in the car's number plate: "))
        num_digits = int(input("Enter the number of digits in the car's number plate: "))
        car = Car(country_code, num_letters, num_digits)
        tracker.add_car(car)

    # Track the cars
    tracker.track_cars()

if __name__ == "__main__":
    main()
