# Using For Loop
def print_multiples_for(n):
    print(f"First 10 multiples of {n} using for loop:")
    for i in range(1, 11):
        print(n * i, end=' ')
    print()
# Using While Loop
def print_multiples_while(n):
    print(f"First 10 multiples of {n} using while loop:")
    i = 1
    while i <= 10:
        print(n * i, end=' ')
        i += 1
    print()
# Example usage:
num = int(input("Enter a number to print its first 10 multiples: "))
print_multiples_for(num)
print_multiples_while(num)