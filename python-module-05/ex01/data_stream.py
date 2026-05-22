#!/usr/bin/env python3

from typing import Any

# importa do ex0 (mesmo diretório ou ajuste o path)
from ex0.data_processor import (
    DataProcessor,
    NumericProcessor,
    TextProcessor,
    LogProcessor,
)


class DataStream:
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []
        self._stats: dict[str, int] = {}

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)
        name = proc.__class__.__name__
        if name not in self._stats:
            self._stats[name] = 0

    def process_stream(self, stream: list[Any]) -> None:
        for element in stream:
            handled = False

            for proc in self._processors:
                if proc.validate(element):
                    proc.ingest(element)
                    name = proc.__class__.__name__
                    self._stats[name] += self._count_items(element)
                    handled = True
                    break

            if not handled:
                print(
                    "DataStream error - Can't process element "
                    f"in stream: {element}"
                )

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")

        if not self._processors:
            print("No processor found, no data")
            return

        for proc in self._processors:
            name = proc.__class__.__name__
            total = self._stats.get(name, 0)
            remaining = proc.size()
            print(
                f"{name.replace('Processor', ' Processor')}: "
                f"total {total} items processed, "
                f"remaining {remaining} on processor"
            )

    @staticmethod
    def _count_items(data: Any) -> int:
        if isinstance(data, list):
            return len(data)
        return 1


# -------------------------
# TEST
# -------------------------
def main() -> None:
    print("=== Code Nexus - Data Stream ===")
    print("Initialize Data Stream...")

    ds = DataStream()
    ds.print_processors_stats()

    print("Registering Numeric Processor")
    num = NumericProcessor()
    ds.register_processor(num)

    stream = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {
                "log_level": "WARNING",
                "log_message": "Telnet access! Use ssh instead",
            },
            {
                "log_level": "INFO",
                "log_message": "User wil is connected",
            },
        ],
        42,
        ["Hi", "five"],
    ]

    print(f"Send first batch of data on stream: {stream}")
    ds.process_stream(stream)
    ds.print_processors_stats()

    print("Registering other data processors")
    text = TextProcessor()
    log = LogProcessor()

    ds.register_processor(text)
    ds.register_processor(log)

    print("Send the same batch again")
    ds.process_stream(stream)
    ds.print_processors_stats()

    print(
        "Consume some elements from the data processors: "
        "Numeric 3, Text 2, Log 1"
    )

    for _ in range(3):
        num.output()

    for _ in range(2):
        text.output()

    for _ in range(1):
        log.output()

    ds.print_processors_stats()


if __name__ == "__main__":
    main()
