def classify_age_nested(age):
    if age >= 0:
        if age <= 12:
            return "Child"
        elif age <= 17:
            return "Teenager"
        elif age <= 64:
            return "Adult"
        else:
            return "Senior"
    else:
        return "Invalid age"
# Explanation:
# The function classify_age_nested uses nested if-elif-else statements to check the age range.
# It first checks if the age is non-negative, then checks each range in order.
# Example usage:
age_input = int(input("Enter age: "))
print("Age group (nested):", classify_age_nested(age_input))
# Now, let's generate the same logic using chained if-elif-else statements (not nested):
def classify_age_chained(age):
    if age < 0:
        return "Invalid age"
    elif age <= 12:
        return "Child"
    elif age <= 19:
        return "Teen"
    elif age <= 59:
        return "Adult"
    else:
        return "Senior"
# Explanation:
# The function classify_age_chained uses a flat if-elif-else structure for clarity and simplicity.
# Example usage:
print("Age group (chained):", classify_age_chained(age_input))
