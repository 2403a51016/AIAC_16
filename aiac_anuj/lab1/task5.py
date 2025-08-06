def letter_frequency(text):
    freq = {}
    for char in text:
        if char.isalpha():
            char = char.lower()
            freq[char] = freq.get(char, 0) + 1
    return freq

if __name__ == "__main__":
    user_input = input("Enter a string: ")
    frequencies = letter_frequency(user_input)
    for letter, count in frequencies.items():
        print(f"{letter}: {count}")