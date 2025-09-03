import unittest
from task5 import convert_date_format
def convert_date_format(date_str):
    import re
    # Check for correct format using regex
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", date_str):
        raise ValueError("Date must be in YYYY-MM-DD format")
    year, month, day = date_str.split('-')
    # Check if all parts are numeric and valid
    if not (year.isdigit() and month.isdigit() and day.isdigit()):
        raise ValueError("Date must contain only numbers")
    return f"{day}-{month}-{year}"
 

class TestConvertDateFormat(unittest.TestCase):
    def test_valid_date(self):
        self.assertEqual(convert_date_format("2023-10-05"), "05-10-2023")
        self.assertEqual(convert_date_format("2000-01-01"), "01-01-2000")
        self.assertEqual(convert_date_format("1999-12-31"), "31-12-1999")

    def test_invalid_format(self):
        with self.assertRaises(ValueError):
            convert_date_format("2023/10/05")
        with self.assertRaises(ValueError):
            convert_date_format("05-10-2023")
        with self.assertRaises(ValueError):
            convert_date_format("2023-10")
        with self.assertRaises(ValueError):
            convert_date_format("2023-10-05-01")

    def test_non_numeric(self):
        with self.assertRaises(ValueError):
            convert_date_format("YYYY-MM-DD")
        with self.assertRaises(ValueError):
            convert_date_format("abcd-ef-gh")

    def test_empty_string(self):
        with self.assertRaises(ValueError):
            convert_date_format("")

if __name__ == "__main__":
    unittest.main()