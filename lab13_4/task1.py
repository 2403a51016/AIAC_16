# Legacy Code with a traditional for loop
numbers = [1, 2, 3, 4, 5]
squares = []
for n in numbers:
    squares.append(n ** 2)
print(f"Legacy code output: {squares}")
# ---
# Refactored Code using a list comprehension
numbers_refactored = [1, 2, 3, 4, 5]
squares_refactored = [n ** 2 for n in numbers_refactored]
print(f"Refactored code output: {squares_refactored}")
# ---
# Example Usage with a different list to show its reusability
example_numbers = [10, 11, 12]
example_squares = [n ** 2 for n in example_numbers]
print(f"Example usage output: {example_squares}")