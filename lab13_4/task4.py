# Refactored Code with Dictionary Mapping
# Define a dictionary to map operation names to functions
operations = {
    "add": lambda x, y: x + y,
    "subtract": lambda x, y: x - y,
    "multiply": lambda x, y: x * y,
    "divide": lambda x, y: x / y,
}
# Legacy variables
operation = "multiply"
a, b = 5, 3
# Use .get() to safely retrieve the function and handle invalid operations
# The second argument to .get() is a default value if the key is not found
operation_func = operations.get(operation, lambda x, y: None)
result = operation_func(a, b)
print(result)
# Example Usage with a different operation
new_operation = "add"
new_a, new_b = 10, 5
new_result = operations.get(new_operation, lambda x, y: None)(new_a, new_b)
print(new_result)