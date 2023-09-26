try:
    result = 10/0
except ZeroDivisionError:
    print("Error: Division by zero")

try:
    x = int(input("Enter a number: "))
    result = 10/x
except ZeroDivisionError:
    print("Error: Division by zero")
except ValueError:
    print("Invalid value, Enter a valid number")
else:
    print(f"Result: {result}")
finally:
    print("Execution finished")

def check_age(age):
    if age < 0:
        raise ValueError("age canot be negative")

try:
    age = -10
    check_age(age)
except ValueError as e:
    print("Error {}".format(e))

class NegativeNumberException(Exception):
    def __init__(self, number):
        super().__init__(f"Negative numbers are not allowed: {number}")
        self.number = number

def calculate_square_root(number):
    if number < 0:
        raise NegativeNumberException(number)
    return number**0.5

try:
    num = float(input("Enter a number: "))
    result = calculate_square_root(num)
    print(f"Square root: {result}")
except NegativeNumberException as e:
    print(f"Error: {e}")
except ValueError:
    print("Invalid input")