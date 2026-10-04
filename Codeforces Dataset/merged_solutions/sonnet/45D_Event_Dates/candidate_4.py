import sys


# --- clause: read_input :: () -> tuple[int, list[tuple[int, int]]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    events = []
    for i in range(n):
        lo = int(data[1 + 2 * i])
        hi = int(data[2 + 2 * i])
        events.append((lo, hi))
    return n, events


# --- clause: assign_dates :: (n: int, events: list[tuple[int, int]]) -> list[int] ---
def assign_dates(n, events):
    order = sorted(range(n), key=lambda i: (events[i][1], events[i][0]))
    taken = set()
    dates = [0] * n
    for i in order:
        window = events[i]
        day = window[0]
        while day in taken:
            day += 1
        taken.add(day)
        dates[i] = day
    return dates


# --- clause: main :: () -> None ---
def main():
    n, events = read_input()
    dates = assign_dates(n, events)
    sys.stdout.write(" ".join([str(day) for day in dates]) + "\n")


if __name__ == "__main__":
    main()
