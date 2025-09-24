# Inefficient Loop
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = []
for i in nums:
    squares.append(i * i)

print(f"Original method: {squares}")

# Refactored with List Comprehension
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares_comprehension = [i * i for i in nums]

print(f"Refactored method: {squares_comprehension}")

# Example Usage with a different list
numbers_to_square = [2, 4, 6, 8]
squared_numbers = [num ** 2 for num in numbers_to_square]

print(f"Squared numbers: {squared_numbers}")