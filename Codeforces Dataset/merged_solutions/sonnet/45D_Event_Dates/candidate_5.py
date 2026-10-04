import sys


# --- clause: read_input :: () -> tuple[int, list[tuple[int, int]]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    events = []
    pos = 1
    for _ in range(n):
        lo = int(data[pos])
        pos += 1
        hi = int(data[pos])
        pos += 1
        events.append((lo, hi))
    return n, events


# --- clause: assign_dates :: (n: int, events: list[tuple[int, int]]) -> list[int] ---
def assign_dates(n, events):
    order = sorted(range(n), key=lambda i: (events[i][1], events[i][0]))
    taken = set()
    dates = [0] * n
    for i in order:
        day = events[i][0]
        while day in taken:
            day += 1
        dates[i] = day
        taken.add(day)
    return dates


# --- clause: main :: () -> None ---
def main():
    n, events = read_input()
    dates = assign_dates(n, events)
    answer = " ".join(map(str, dates))
    sys.stdout.write(answer + "\n")


if __name__ == "__main__":
    main()
