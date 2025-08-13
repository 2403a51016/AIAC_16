def format_names(names):
    formatted = []
    for name in names:
        parts = name.strip().split()
        if len(parts) >= 2:
            first_name = parts[0]
            last_name = parts[-1]
            formatted.append(f"{name} : first name – {first_name.lower()} , last name – {last_name.lower()}")
        else:
            formatted.append(f"{name} : Invalid name format")
    return formatted

# Take input from user
n = int(input("Enter number of names: "))
names_list = []
for _ in range(n):
    names_list.append(input("Enter name: "))

for line in format_names(names_list):
    print(line)