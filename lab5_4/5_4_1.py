# Python script to collect user data (name, age, email)

def collect_user_data_from_file(file_path):
    """
    Expects a text file with lines in the format:
    name: John Doe
    age: 30
    email: john@example.com
    """
    user_data = {}
    try:
        with open(file_path, 'r') as f:
            for line in f:
                if ':' in line:
                    key, value = line.strip().split(':', 1)
                    user_data[key.strip().lower()] = value.strip()
    except FileNotFoundError:
        print("File not found. Please check the path.")
        return None
    except Exception as e:
        print("An error occurred:", e)
        return None
    return user_data


file_path = input("Enter the path to the user data file: ")
user_data = collect_user_data_from_file(file_path)
if user_data:
    "C:\Users\ANUJ\OneDrive\Desktop\AIAC\lab5_4\file.txt"
    print("User data collected from file:", user_data)

# How to anonymize or protect this data:
# - Do not store sensitive data (like email) in plain text.
# - You can hash the email before storing it, e.g.:
#     import hashlib
#     hashed_email = hashlib.sha256(user_data['email'].encode()).hexdigest()
#     user_data['email'] = hashed_email
# - Avoid storing the name if not necessary, or replace it with a pseudonym.
# - Store data in encrypted files or databases.
# - Only collect and retain data that is absolutely necessary.
# - Ensure file permissions restrict unauthorized access to the data file.
