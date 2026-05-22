#!/usr/bin/env python3

import sys
from typing import TextIO


def ft_ancient_text(filename: str) -> None:
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'...")
    print("---")

    try:
        f: TextIO = open(filename, "r")
        try:
            for line in f:
                print(line, end="")
        finally:
            f.close()
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error opening file '{filename}': {e}")
        return

    print("---")
    print(f"File '{filename}' closed.")


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    ft_ancient_text(sys.argv[1])


if __name__ == "__main__":
    main()
