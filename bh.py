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


This code defines a function add_numbers that takes two arguments and returns their sum. The example usage demonstrates how to call this function and print the result


Sure! Here are three different ways to generate the Fibonacci series in Python:

1. Using Iteration
def fibonacci_iterative(n):
    fib_series = [0, 1]
    for i in range(2, n):
        next_value = fib_series[-1] + fib_series[-2]
        fib_series.append(next_value)
    return fib_series[:n]

# Example usage:
n = 10
print(fibonacci_iterative(n))

2. Using Recursion
def fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_series = fibonacci_recursive(n-1)
        fib_series.append(fib_series[-1] + fib_series[-2])
        return fib_series

# Example usage:
n = 10
print(fibonacci_recursive(n))

3. Using a Generator
def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Example usage:
n = 10
print(list(fibonacci_generator(n)))


Feel free to choose the method that best suits your needs!.
