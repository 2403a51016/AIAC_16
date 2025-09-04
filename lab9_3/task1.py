def sum_even_odd(numbers):
    """
    Calculates the sum of even and odd numbers in a given list.

    Args:
        numbers (list of int): A list of integers to be processed.

    Returns:
        tuple: A tuple containing two integers:
            - The sum of even numbers in the list.
            - The sum of odd numbers in the list.

    Example:
        >>> sum_even_odd([1, 2, 3, 4, 5, 6])
        (12, 9)
    """
    # Calculate the sum of even numbers using a generator expression
    even_sum = sum(num for num in numbers if num % 2 == 0)
    # Calculate the sum of odd numbers using a generator expression
    odd_sum = sum(num for num in numbers if num % 2 != 0)
    # Return a tuple containing the sums
    return even_sum, odd_sum

if __name__ == "__main__":
    # Define a sample list of numbers
    sample_numbers = [1, 2, 3, 4, 5, 6]
    # Call the function and unpack the results
    even_sum, odd_sum = sum_even_odd(sample_numbers)
    # Print the sum of even numbers
    print(f"Sum of even numbers: {even_sum}")
    # Print the sum of odd numbers
    print(f"Sum of odd numbers: {odd_sum}")
