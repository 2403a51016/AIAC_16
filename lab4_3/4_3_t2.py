def cm_to_inches(cm):
    """
    Convert centimeters to inches.

    Args:
        cm (float): Length in centimeters.

    Returns:
        float: Length in inches.
    """
    return round(cm / 2.54, 2)

# Example usage:
if __name__ == "__main__":
    cm_value = float(input("Enter length in centimeters: "))
    inches = cm_to_inches(cm_value)
    print(f"{cm_value} cm = {inches} inches")