def sort_list(data):
    try:
        return sorted(data)
    except TypeError as e:
        print("TypeError while sorting:", e)
        return None

items = [3, "apple", 1, "banana", 2]
result = sort_list(items)
if result is not None:
    print(result)
else:
    print("Sorting failed due to incompatible data types.")
