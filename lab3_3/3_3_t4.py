def user_system():
    users = {}

    def register_user(username, password):
        if username in users:
            return "Username already exists."
        users[username] = password
        return "User registered successfully."

    def login_user(username, password):
        if username not in users:
            return "Username not found."
        if users[username] != password:
            return "Incorrect password."
        return "Login successful."

    return register_user, login_user

# Example usage:
register_user, login_user = user_system()
print(register_user("alice", "password123"))  # User registered successfully.
print(login_user("alice", "password123"))     # Login successful.
print(login_user("bob", "pass"))              # Username not found.