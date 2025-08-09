import random

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Generate a random number between 1 and 10
num = random.randint(1, 10)
print(f"Random number: {num}")
print(f"Factorial of {num} is {factorial(num)}")