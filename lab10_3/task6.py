def grade(score):
    """
    Returns a letter grade based on the numeric score.
    Args:
        score (int or float): The score to evaluate.
    Returns:
        str: A letter grade from A to F.
    """
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
# Example usage
print(grade(85))  # Output: B