from typing import Iterable


def count_vowels(text: str) -> int:
    """Return the number of vowels (a, e, i, o, u) in the given string."""
    vowels: set[str] = {"a", "e", "i", "o", "u"}
    lower_text = text.lower()
    return sum(1 for ch in lower_text if ch in vowels)


if __name__ == "__main__":
    user_input = input("Enter a string: ")
    print(count_vowels(user_input))


