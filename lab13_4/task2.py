# Legacy Code
words = ["AI", "helps", "in", "refactoring", "code"]
sentence = ""
for word in words:
    sentence += word + " "
print(f"Legacy code output: '{sentence.strip()}'")
# ---
# Refactored Code with str.join()
words_refactored = ["AI", "helps", "in", "refactoring", "code"]
sentence_refactored = " ".join(words_refactored)
print(f"Refactored code output: '{sentence_refactored}'")
# ---
# Example Usage
# Imagine you have a list of phrases for a greeting
greeting_parts = ["Hello", "world", "this", "is", "a", "test"]
full_greeting = " ".join(greeting_parts)
print(f"Example usage: '{full_greeting}'")