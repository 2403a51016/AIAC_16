def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = sum(1 for char in s if char in vowels)
    return count

# Example usage:
input_str = input("Enter a string: ")
vowel_count = count_vowels(input_str)
print(f"{input_str} has {vowel_count} vowels.")