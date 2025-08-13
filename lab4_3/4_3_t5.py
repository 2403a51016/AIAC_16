file_path = r"C:\Users\ANUJ\OneDrive\Desktop\exam.txt.txt"

def count_lines(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            return len(lines)
    except FileNotFoundError:
        print(f"File not found: {path}")
        return 0

num_lines = count_lines(file_path)
print(f"{file_path} has {num_lines} lines")