def cm_to_inches(centimeters: float) -> float:
    """
    Convert centimeters to inches.

    Uses the exact conversion: 1 inch = 2.54 centimeters.
    Returns the raw float result; format on display as needed.
    """
    return centimeters / 2.54


if __name__ == "__main__":
    try:
        cm_input = input("Enter length in centimeters: ")
        cm_value = float(cm_input)
    except ValueError:
        print("Please enter a valid number for centimeters.")
    else:
        inches_value = cm_to_inches(cm_value)
        print(f"{cm_value:g} cm = {inches_value:.2f} inches")


