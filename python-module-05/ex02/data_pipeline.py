#!/usr/bin/env python3

from typing import Any, Protocol

from ex0.data_processor import (
    DataProcessor,
    NumericProcessor,
    TextProcessor,
    LogProcessor,
)


# -------------------------
# EXPORT PLUGIN (DUCK TYPING)
# -------------------------
class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


# -------------------------
# CSV PLUGIN
# -------------------------
class CSVExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        values = [value for _, value in data]
        print("CSV Output:")
        safe_values = [v.replace(",", "\\,") for v in values]
        print(",".join(safe_values))


# -------------------------
# JSON PLUGIN
# -------------------------
class JSONExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        items = []
        for rank, value in data:
            safe_value = value.replace('"', '\\"')
            items.append(f'"item_{rank}": "{safe_value}"')

        print("JSON Output:")
        print("{" + ", ".join(items) + "}")


# -------------------------
# DATA STREAM
# -------------------------
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
                    "DataStream error - "
                    f"Can't process element in stream: {element}"
                )

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self._processors:
            extracted: list[tuple[int, str]] = []

            for _ in range(nb):
                try:
                    extracted.append(proc.output())
                except RuntimeError:
                    break

            if extracted:
                plugin.process_output(extracted)

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
    print("=== Code Nexus - Data Pipeline ===")
    print("Initialize Data Stream...")

    ds = DataStream()
    ds.print_processors_stats()

    print("Registering Processors")
    num = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()

    ds.register_processor(num)
    ds.register_processor(text)
    ds.register_processor(log)

    stream1 = [
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

    print(f"Send first batch of data on stream: {stream1}")
    ds.process_stream(stream1)
    ds.print_processors_stats()

    print("Send 3 processed data from each processor to a CSV plugin:")
    csv_plugin = CSVExportPlugin()
    ds.output_pipeline(3, csv_plugin)
    ds.print_processors_stats()

    stream2 = [
        21,
        ["I love AI", "LLMs are wonderful", "Stay healthy"],
        [
            {"log_level": "ERROR", "log_message": "500 server crash"},
            {
                "log_level": "NOTICE",
                "log_message": "Certificate expires in 10 days",
            },
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello",
    ]

    print(f"Send another batch of data: {stream2}")
    ds.process_stream(stream2)
    ds.print_processors_stats()

    print("Send 5 processed data from each processor to a JSON plugin:")
    json_plugin = JSONExportPlugin()
    ds.output_pipeline(5, json_plugin)
    ds.print_processors_stats()


if __name__ == "__main__":
    main()
