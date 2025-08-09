def sum_of_squares_in_range():
    """Calculates the sum of squares of numbers within a given range.
    Takes range input from the user.
    Returns a tuple of (result, start, end) or (None, None, None) if error occurs.
    """
    try:
        # Get input from user
        start = int(input("Enter the start of the range: "))
        end = int(input("Enter the end of the range: "))
        
        # Validate input
        if start > end:
            print("Error: Start value should be less than or equal to end value.")
            return None, None, None
        
        # Calculate sum of squares
        total = 0
        for num in range(start, end + 1):
            total += num ** 2
        
        return total, start, end
    
    except ValueError:
        print("Error: Please enter valid integers.")
        return None, None, None

def main():
    """
    Main function to run the sum of squares calculator.
    """
    print("Sum of Squares Calculator")
    print("=" * 25)
    
    result, start, end = sum_of_squares_in_range()
    
    if result is not None:
        print(f"\nThe sum of squares from {start} to {end} is: {result}")
    else:
        print("\nCalculation failed. Please try again.")

if __name__ == "__main__":
    main()
