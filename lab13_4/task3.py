# Legacy Code
student_scores = {"Alice": 85, "Bob": 90}
if "Charlie" in student_scores:
    print(student_scores["Charlie"])
else:
    print("Not Found")
# Refactored Code with .get()
student_scores_refactored = {"Alice": 85, "Bob": 90}
score = student_scores_refactored.get("Charlie", "Not Found")
print(score)
# Example Usage to show a successful lookup
# Looking up an existing key, "Alice"
existing_score = student_scores_refactored.get("Alice", "Not Found")
print(f"Alice's score: {existing_score}")