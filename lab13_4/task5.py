# Legacy Code
items = [10, 20, 30, 40, 50]
found = False
for i in items:
    if i == 30:
        found = True
        break
print("Found" if found else "Not Found")
# Refactored Code with 'in' keyword
items_refactored = [10, 20, 30, 40, 50]
if 30 in items_refactored:
    print("Found")
else:
    print("Not Found")
# Example Usage to show "Not Found" case
another_list = [1, 2, 3, 4, 5]
if 99 in another_list:
    print("Found")
else:
    print("Not Found")