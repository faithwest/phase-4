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
