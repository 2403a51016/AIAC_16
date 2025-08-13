import os


def count_lines_in_file(file_path: str) -> int:
    """Return the number of lines in the file at the given path."""
    line_count = 0
    with open(file_path, "r", encoding="utf-8", errors="ignore") as file_handle:
        for _ in file_handle:
            line_count += 1
    return line_count


def format_line_count_message(file_path: str) -> str:
    file_name = os.path.basename(file_path)
    total_lines = count_lines_in_file(file_path)
    return f"{file_name} has {total_lines} lines."


if __name__ == "__main__":
    # Example path (Windows): C:\\Users\\ANUJ\\OneDrive\\Desktop\\exam.txt.txt
    user_path = input("Enter the full path to the .txt file: ").strip().strip('"')
    if not user_path:
        print("No file path provided.")
    else:
        try:
            print(format_line_count_message(user_path))
        except FileNotFoundError:
            print(f"File not found: {user_path}")
        except PermissionError:
            print(f"Permission denied: {user_path}")
        except OSError as os_error:
            print(f"Error reading file: {os_error}")


