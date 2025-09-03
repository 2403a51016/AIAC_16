def convert_date_format(date_str):
    """
    Converts a date string from "YYYY-MM-DD" to "DD-MM-YYYY" format.

    Args:
        date_str (str): Date string in "YYYY-MM-DD" format.

    Returns:
        str: Date string in "DD-MM-YYYY" format.
    """
    parts = date_str.split('-')
    if len(parts) != 3:
        raise ValueError("Input date must be in 'YYYY-MM-DD' format")
    year, month, day = parts
    return f"{day}-{month}-{year}"
# Example usage:
date_input = "2023-10-05"
converted_date = convert_date_format(date_input)
print(converted_date)  # Output: "05-10-2023"
