def find_largest_of_three():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    c = float(input("Enter third number: "))
    largest = max(a, b, c)
    return largest

# Example usage:
result = find_largest_of_three()
print("The largest value is:", result)