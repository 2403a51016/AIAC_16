import unittest
from task1 import is_valid_email
class TestEmailValidation(unittest.TestCase):
    def test_valid_emails(self):
        valid_emails = [
            "user@example.com",
            "john.doe@domain.co.uk",
            "a_b.c-d@sub.domain.com",
            "simple@domain.org",
        ]
        for email in valid_emails:
            self.assertTrue(is_valid_email(email), f"Failed for {email}")

    def test_invalid_emails(self):
        invalid_emails = [
            "userexample.com",          # missing @
            "user@@example.com",        # two @
            # Add other invalid cases as needed
        ]
        for email in invalid_emails:
            self.assertFalse(is_valid_email(email), f"Failed for {email}")

            def test_edge_cases(self):
                # Emails that start or end with special characters
                self.assertFalse(is_valid_email(".user@domain.com"))
                self.assertFalse(is_valid_email("user.@domain.com"))
                self.assertFalse(is_valid_email("_user@domain.com"))
                self.assertFalse(is_valid_email("user_@domain.com"))
                self.assertFalse(is_valid_email("user@domain.com."))
                self.assertFalse(is_valid_email("user@.domain.com"))
                self.assertFalse(is_valid_email("user@domain..com"))
                self.assertFalse(is_valid_email("user@domaincom"))
                self.assertFalse(is_valid_email("@domain.com"))
                self.assertFalse(is_valid_email("user@"))
                self.assertFalse(is_valid_email("user@domain,com"))
                self.assertFalse(is_valid_email("user@domain@com"))
                self.assertTrue(is_valid_email("user.name@domain.com"))
                self.assertTrue(is_valid_email("user_name@domain.com"))

if __name__ == "__main__":
    unittest.main()