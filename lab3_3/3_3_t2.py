def input_numbers():
    nums = input("Enter numbers separated by spaces: ")
    return [int(x) for x in nums.split()]

def sort_ascending(numbers):
    return sorted(numbers)

def sort_descending(numbers):
    return sorted(numbers, reverse=True)

def sort_even(numbers):
    return sorted([x for x in numbers if x % 2 == 0])

def sort_odd(numbers):
    return sorted([x for x in numbers if x % 2 != 0])

def main():
    numbers = []
    while True:
        print("\nMenu:")
        print("1. Input numbers")
        print("2. Sort in ascending order")
        print("3. Sort in descending order")
        print("4. Show even numbers (sorted)")
        print("5. Show odd numbers (sorted)")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            numbers = input_numbers()
        elif choice == '2':
            if numbers:
                print("Ascending order:", sort_ascending(numbers))
            else:
                print("Please input numbers first.")
        elif choice == '3':
            if numbers:
                print("Descending order:", sort_descending(numbers))
            else:
                print("Please input numbers first.")
        elif choice == '4':
            if numbers:
                print("Even numbers (sorted):", sort_even(numbers))
            else:
                print("Please input numbers first.")
        elif choice == '5':
            if numbers:
                print("Odd numbers (sorted):", sort_odd(numbers))
            else:
                print("Please input numbers first.")
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()