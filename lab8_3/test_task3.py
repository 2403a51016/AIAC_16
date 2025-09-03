import unittest
from task3 import is_sentence_palindrome

class TestIsSentencePalindrome(unittest.TestCase):
    def test_simple_palindrome(self):
        self.assertTrue(is_sentence_palindrome("madam"))

    def test_sentence_palindrome(self):
        self.assertTrue(is_sentence_palindrome("A man, a plan, a canal: Panama"))

    def test_not_palindrome(self):
        self.assertFalse(is_sentence_palindrome("Hello, world!"))

    def test_empty_string(self):
        self.assertTrue(is_sentence_palindrome(""))

    def test_single_character(self):
        self.assertTrue(is_sentence_palindrome("x"))

    def test_palindrome_with_numbers(self):
        self.assertTrue(is_sentence_palindrome("12321"))

    def test_mixed_case_and_symbols(self):
        self.assertTrue(is_sentence_palindrome("No 'x' in Nixon"))

    def test_non_palindrome_with_symbols(self):
        self.assertFalse(is_sentence_palindrome("Python 3.8!"))

    def test_palindrome_with_spaces(self):
        self.assertTrue(is_sentence_palindrome("nurses run"))

    def test_palindrome_with_unicode(self):
        self.assertTrue(is_sentence_palindrome("А роза упала на лапу Азора"))  # Cyrillic palindrome

    def test_long_non_palindrome(self):
        self.assertFalse(is_sentence_palindrome("This is definitely not a palindrome sentence."))

    def test_palindrome_with_mixed_alphanumeric(self):
        self.assertTrue(is_sentence_palindrome("1a2b2a1"))

    def test_palindrome_with_only_symbols(self):
        self.assertTrue(is_sentence_palindrome("!!!"))  # No alphanumeric, so cleaned is empty, which is a palindrome

    def test_palindrome_with_leading_and_trailing_spaces(self):
        self.assertTrue(is_sentence_palindrome("   racecar   "))

    def test_palindrome_with_tabs_and_newlines(self):
        self.assertTrue(is_sentence_palindrome("\n\tEva, can I see bees in a cave?\t\n"))

if __name__ == "__main__":
    unittest.main()