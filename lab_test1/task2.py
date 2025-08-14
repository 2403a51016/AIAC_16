import re

def extract_emails(text):
    # Simple approach: split by spaces and look for '@' in each word
    words = text.split()
    emails = [word.strip('.,;:') for word in words if '@' in word]
    return emails

if __name__ == "__main__":
    sample_text = """
    Please contact us at support@example.com for further information.
    You can also reach out to admin123@domain.co.uk or sales-info@company.org.
    """
    emails = extract_emails(sample_text)
    print("Extracted email addresses:")
    for email in emails:
        print(email)