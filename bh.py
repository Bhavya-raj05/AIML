Sure! An Armstrong number (also known as a narcissistic number) is a number that is equal to the sum of its own digits each raised to the power of the number of digits. Here's a Python code snippet to check if a number is an Armstrong number:

def is_armstrong_number(num):
    # Convert the number to a string to easily iterate over digits
    num_str = str(num)
    # Calculate the number of digits
    num_digits = len(num_str)
    # Initialize the sum
    sum_of_powers = 0
    
    # Iterate over each digit in the number
    for digit in num_str:
        # Convert the digit back to an integer and raise it to the power of num_digits
        sum_of_powers += int(digit) ** num_digits
    
    # Check if the sum of the powers is equal to the original number
    return sum_of_powers == num

# Example usage
number = 153
if is_armstrong_number(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")


This code defines a function is_armstrong_number that takes a number as input and checks if it is an Armstrong number. The example usage checks if 153 is an Armstrong number and prints the result. Feel free to test it with other numbers!



Sure! Here is a simple Python code snippet to add two numbers:

# Function to add two numbers
def add_numbers(a, b):
    return a + b

# Example usage
num1 = 5
num2 = 3
result = add_numbers(num1, num2)
print(f"The sum of {num1} and {num2} is {result}")


This code defines a function add_numbers that takes two arguments and returns their sum. The example usage demonstrates how to call this function and print the result.
