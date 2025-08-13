def count_vowels(text: str) -> int:
    """Return the number of vowels (a, e, i, o, u) in the given string."""
    vowels = {"a", "e", "i", "o", "u"}
    return sum(1 for ch in text.lower() if ch in vowels)


def format_vowel_count(text: str) -> str:
    return f"{text} has {count_vowels(text)} vowels."


if __name__ == "__main__":
    user_input = input("Enter a string: ")
    print(format_vowel_count(user_input))


