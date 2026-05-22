import random
from typing import Generator


def gen_event() -> Generator[tuple[str, str], None, None]:
    players = ["alice", "bob", "charlie", "dylan"]
    actions = [
        "run", "eat", "sleep", "grab",
        "move", "climb", "swim", "use",
        "release",
    ]

    while True:
        name = random.choice(players)
        action = random.choice(actions)
        yield (name, action)


def consume_event(
    events: list[tuple[str, str]],
) -> Generator[tuple[str, str], None, None]:
    while len(events) > 0:
        idx = random.randrange(len(events))
        yield events.pop(idx)


print("=== Game Data Stream Processor ===")

event_gen = gen_event()

for i in range(1000):
    event = next(event_gen)
    print(
        f"Event {i}: Player {event[0]} "
        f"did action {event[1]}"
    )

event_list: list[tuple[str, str]] = []

for _ in range(10):
    event_list.append(next(event_gen))

print("Built list of 10 events:", event_list)

for event in consume_event(event_list):
    print("Got event from list:", event)
    print("Remains in list:", event_list)
