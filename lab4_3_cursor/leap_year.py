def is_leap_year(year: int) -> bool:
    """
    Return True if the provided year is a leap year, otherwise False.

    Rules:
    - Years divisible by 4 are leap years,
    - Except years divisible by 100, which are not,
    - Unless they are divisible by 400, which are leap years.
    """
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return year % 4 == 0


if __name__ == "__main__":
    try:
        year_input = input("Enter a year: ")
        year_value = int(year_input)
    except ValueError:
        print("Please enter a valid integer year.")
    else:
        if is_leap_year(year_value):
            print(f"{year_value} is a leap year.")
        else:
            print(f"{year_value} is not a leap year.")


