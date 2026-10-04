import sys


# --- clause: read_input :: () -> tuple[int, list[tuple[int, int]]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    events = []
    idx = 1
    for _ in range(n):
        lo, hi = int(data[idx]), int(data[idx + 1])
        idx += 2
        events.append((lo, hi))
    return n, events


# --- clause: assign_dates :: (n: int, events: list[tuple[int, int]]) -> list[int] ---
def assign_dates(n, events):
    order = sorted(range(n), key=lambda i: (events[i][1], events[i][0]))
    taken = set()
    dates = [0] * n
    for i in order:
        lo, hi = events[i]
        day = lo
        while day in taken:
            day = day + 1
        taken.add(day)
        dates[i] = day
    return dates


# --- clause: main :: () -> None ---
def main():
    n, events = read_input()
    dates = assign_dates(n, events)
    sys.stdout.write("%s\n" % " ".join(map(str, dates)))


if __name__ == "__main__":
    main()
