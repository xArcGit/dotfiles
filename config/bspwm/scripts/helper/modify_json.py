import sys
from typing import List


def add_text_to_json(file_path: str, new_text: str) -> None:
    key_to_remove = new_text.split(":")[0].strip()  # Extract key from new text

    with open(file_path, "r") as file:
        lines: List[str] = file.readlines()

    new_lines: List[str] = []
    for line in lines:
        if line.strip().startswith(key_to_remove):
            continue  # Skip lines starting with the key to remove
        stripped_line = line.strip()
        if stripped_line == "}":
            last_non_empty_line = new_lines[-1].rstrip()
            if last_non_empty_line.endswith(","):
                new_lines[-1] = f"{last_non_empty_line}\n"
            else:
                new_lines[-1] = f"{last_non_empty_line},\n"
            new_lines.append(f"  {new_text}\n")
            new_lines.append("}\n")
        else:
            new_lines.append(
                line if line.strip() else "\n"
            )  # Preserve blank lines for formatting

    with open(file_path, "w") as file:
        file.writelines(new_lines)


def main() -> None:
    if len(sys.argv) != 3:
        print("Usage: python script_name.py <file_path> <text>")
        return

    file_path: str = sys.argv[1]
    new_text: str = sys.argv[2]
    add_text_to_json(file_path, new_text)
    print(f"\033[0;32m{new_text} added successfully. \033[0m")


if __name__ == "__main__":
    main()
