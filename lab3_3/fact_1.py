def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

try:
    num = int(input("Enter a number: "))
    print(f"Factorial of {num} is {factorial(num)}")
except ValueError:
    print("Please enter a valid integer.")