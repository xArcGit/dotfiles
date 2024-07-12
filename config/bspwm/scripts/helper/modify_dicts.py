import sys
import os
import re

# ANSI color codes for colored output
RED = "\033[0;31m"
GREEN = "\033[0;32m"
YELLOW = "\033[1;33m"
NC = "\033[0m"  # No Color


def add_colored_text(text: str, color: str = GREEN) -> str:
    return f"{color}{text}{NC}"


def read_file(file_path: str) -> str:
    try:
        with open(file_path, "r") as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(add_colored_text(f"Error: File not found: {file_path}", RED))
        sys.exit(1)
    except Exception as e:
        print(add_colored_text(f"Error reading file: {e}", RED))
        sys.exit(1)


def write_file(file_path: str, content: str) -> None:
    try:
        with open(file_path, "w") as file:
            file.write(content)
    except Exception as e:
        print(add_colored_text(f"Error writing to file: {e}", RED))
        sys.exit(1)


def modify_dict_in_file(file_path: str, dict_name: str, new_data: str) -> None:
    content = read_file(file_path)

    # Define pattern for dictionary
    dict_pattern = re.compile(
        rf"^{re.escape(dict_name)}:\s*Dict\[str, str\]\s*=\s*{{\s*(.*?)\s*}}",
        re.DOTALL | re.MULTILINE,
    )

    # Function to replace old data with new data
    def replacer(match: re.Match[str]) -> str:
        return f"{dict_name}: Dict[str, str] = {{\n{new_data}\n}}"

    # Perform replacement in content
    content = re.sub(dict_pattern, replacer, content)

    write_file(file_path, content)
    print(add_colored_text(f"Modified {dict_name} in file: {file_path}", GREEN))


if __name__ == "__main__":
    if len(sys.argv) < 4 or len(sys.argv) % 2 != 0:
        print(
            add_colored_text(
                "Usage: python modify_dicts_in_file.py <file_path> <dict_name1> <new_data1> [<dict_name2> <new_data2> ...]",
                YELLOW,
            )
        )
        sys.exit(1)

    file_path = sys.argv[1]
    updates = [
        (sys.argv[i], sys.argv[i + 1].replace(r"\n", "\n"))
        for i in range(2, len(sys.argv), 2)
    ]

    if not os.path.isfile(file_path):
        print(
            add_colored_text(
                f"Error: The path provided is not a file: {file_path}", RED
            )
        )
        sys.exit(1)

    for dict_name, new_data in updates:
        modify_dict_in_file(file_path, dict_name, new_data)
