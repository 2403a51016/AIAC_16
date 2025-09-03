import string

def is_sentence_palindrome(sentence):
    cleaned = ''.join(
        c.lower() for c in sentence if c.isalnum()
    )
    return cleaned == cleaned[::-1]
if __name__ == "__main__":
        example = "A man, a plan, a canal: Panama"
        print(f"Is the sentence a palindrome? {is_sentence_palindrome(example)}")