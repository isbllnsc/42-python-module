#!/usr/bin/env python3

import sys
from typing import TextIO


def read_file(filename: str) -> list[str] | None:
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")
    print("---")

    try:
        f: TextIO = open(filename, "r")
        try:
            lines = f.readlines()
            for line in lines:
                print(line, end="")
        finally:
            f.close()
    except OSError as e:
        print(f"Error opening file '{filename}': {e}")
        return None

    print("---")
    print(f"File '{filename}' closed.")
    return lines


def transform_data(lines: list[str]) -> list[str]:
    print("Transform data:")
    print("---")

    new_lines: list[str] = []

    for line in lines:
        if line.endswith("\n"):
            new_line = line[:-1] + "#\n"
        else:
            new_line = line + "#"
        new_lines.append(new_line)
        print(new_line, end="")

    print("---")
    return new_lines


def save_file(lines: list[str]) -> None:
    filename = input("Enter new file name (or empty): ")

    if filename == "":
        print("Not saving data.")
        return

    print(f"Saving data to '{filename}'")

    try:
        f: TextIO = open(filename, "w")
        try:
            for line in lines:
                f.write(line)
        finally:
            f.close()
    except OSError as e:
        print(f"Error writing file '{filename}': {e}")
        return

    print(f"Data saved in file '{filename}'.")


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
        return

    lines = read_file(sys.argv[1])
    if lines is None:
        return

    new_lines = transform_data(lines)
    save_file(new_lines)


if __name__ == "__main__":
    main()
