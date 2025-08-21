def sum_to_n(n):
   
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# Explanation:
# The function sum_to_n(n) initializes a variable total to 0.
# It then iterates from 1 to n (inclusive) using a for loop, adding each number to total.
# Finally, it returns the computed sum.

# Example usage:
num = int(input("Enter a number to calculate the sum of first n natural numbers: "))
print(f"Sum of first {num} natural numbers (using for loop):", sum_to_n(num))

# Alternative approach using a while loop:
def sum_to_n_while(n):
    
    total = 0
    i = 1
    while i <= n:
        total += i
        i += 1
    return total

print(f"Sum of first {num} natural numbers (using while loop):", sum_to_n_while(num))

# Suggestions for other controlled looping:
# - You can use Python's built-in sum() and range() for a more concise solution: sum(range(1, n+1))
# - For very large n, you can use the mathematical formula: n * (n + 1) // 2 for O(1) time.
# - You can also use recursion, though it's not recommended for large n due to recursion limits.
