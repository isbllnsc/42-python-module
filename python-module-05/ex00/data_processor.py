#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._storage: list[str] = []
        self._counter = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def size(self) -> int:
        return len(self._storage)

    def output(self) -> tuple[int, str]:
        if not self._storage:
            raise RuntimeError("No data to output")

        value = self._storage.pop(0)
        rank = self._counter
        self._counter += 1
        return rank, value


# -------------------------
# NUMERIC PROCESSOR
# -------------------------
class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            return all(isinstance(x, (int, float)) for x in data)
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")

        if isinstance(data, list):
            for value in data:
                self._storage.append(str(value))
        else:
            self._storage.append(str(data))


# -------------------------
# TEXT PROCESSOR
# -------------------------
class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(x, str) for x in data)
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")

        if isinstance(data, list):
            self._storage.extend(data)
        else:
            self._storage.append(data)


# -------------------------
# LOG PROCESSOR
# -------------------------
class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        def is_valid_dict(d: Any) -> bool:
            return (
                isinstance(d, dict)
                and all(
                    isinstance(k, str) and isinstance(v, str)
                    for k, v in d.items()
                )
            )

        if is_valid_dict(data):
            return True

        if isinstance(data, list):
            return all(is_valid_dict(x) for x in data)

        return False

    def ingest(
        self,
        data: dict[str, str] | list[dict[str, str]],
    ) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")

        def format_log(d: dict[str, str]) -> str:
            return (
                f"{d.get('log_level', '')}: "
                f"{d.get('log_message', '')}"
            )

        if isinstance(data, list):
            for entry in data:
                self._storage.append(format_log(entry))
        else:
            self._storage.append(format_log(data))


# -------------------------
# TEST
# -------------------------
def main() -> None:
    print("=== Code Nexus - Data Processor ===")

    # Numeric
    print("Testing Numeric Processor...")
    num = NumericProcessor()
    print("Trying to validate input '42':", num.validate(42))
    print("Trying to validate input 'Hello':", num.validate("Hello"))

    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        num.ingest("foo")  # type: ignore[arg-type]
    except Exception as exc:
        print("Got exception:", exc)

    print("Processing data:", [1, 2, 3, 4, 5])
    num.ingest([1, 2, 3, 4, 5])

    print("Extracting 3 values...")
    for _ in range(3):
        rank, value = num.output()
        print(f"Numeric value {rank}: {value}")

    # Text
    print("Testing Text Processor...")
    text = TextProcessor()
    print("Trying to validate input '42':", text.validate(42))

    print("Processing data:", ["Hello", "Nexus", "World"])
    text.ingest(["Hello", "Nexus", "World"])

    print("Extracting 1 value...")
    rank, value = text.output()
    print(f"Text value {rank}: {value}")

    # Log
    print("Testing Log Processor...")
    log = LogProcessor()
    print("Trying to validate input 'Hello':", log.validate("Hello"))

    logs = [
        {"log_level": "NOTICE", "log_message": "Connection to server"},
        {"log_level": "ERROR", "log_message": "Unauthorized access!!"},
    ]

    print("Processing data:", logs)
    log.ingest(logs)

    print("Extracting 2 values...")
    for _ in range(2):
        rank, value = log.output()
        print(f"Log entry {rank}: {value}")


if __name__ == "__main__":
    main()
