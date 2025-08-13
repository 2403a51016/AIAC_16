from typing import List


def format_names(full_name_list: List[str]) -> str:
    """
    Format a list of full names into lines showing first and last names.

    Each output line looks like:
    "Full Name: first name - <first>, last name - <last>"

    - First and last names are lowercased for consistency with the example.
    - Extra spaces are normalized.
    - If only one token exists, last name is left empty.
    """
    formatted_lines: List[str] = []

    for full_name in full_name_list:
        if not isinstance(full_name, str):
            continue

        # Normalize spaces (collapse multiple spaces and trim ends)
        normalized_full_name = " ".join(full_name.split())
        if not normalized_full_name:
            continue

        parts = normalized_full_name.split(" ")
        first_name = parts[0].lower()
        last_name = parts[-1].lower() if len(parts) > 1 else ""

        if last_name:
            formatted_lines.append(
                f"{normalized_full_name}: first name - {first_name} , last name - {last_name}"
            )
        else:
            formatted_lines.append(
                f"{normalized_full_name}: first name - {first_name} , last name - "
            )

    return "\n".join(formatted_lines)


if __name__ == "__main__":
    sample = ["Narendra Modi", "Rahul Gandhi"]
    print(format_names(sample))


