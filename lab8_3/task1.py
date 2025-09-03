import re
def is_valid_email(email):
    # Check if email contains exactly one '@' character
    if email.count('@') != 1:
        return False
    
    # Check if email starts or ends with special characters
    if re.match(r'^[\W_]|[\W_]$', email):
        return False
    
    # Check if email contains at least one '.' character after '@'
    _, domain_part = email.split('@')
    if '.' not in domain_part:
        return False
    
    return True
emails = [
        "user@example.com",
        "user.name@domain.co",
        "user@domain",
        "@example.com",
        "user@.com",
        "user@domain.com.",
        "user@@domain.com"
    ]
for email in emails:
        print(f"{email}: {is_valid_email(email)}")