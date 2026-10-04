import sys


# --- clause: read_input :: () -> list[tuple[int, int, list[tuple[int, int]]]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    reader = 1
    cases = []
    for _ in range(t):
        n = numbers[reader]
        h = numbers[reader + 1]
        m = numbers[reader + 2]
        reader += 3
        alarms = []
        for _ in range(n):
            alarms.append((numbers[reader], numbers[reader + 1]))
            reader += 2
        cases.append((h, m, alarms))
    return cases


# --- clause: sleep_time :: (h: int, m: int, alarms: list[tuple[int, int]]) -> tuple[int, int] ---
def sleep_time(h, m, alarms):
    bed = h * 60 + m
    waits = []
    for hour, minute in alarms:
        moment = hour * 60 + minute
        waits.append(moment - bed if moment >= bed else moment + 24 * 60 - bed)
    best = min(waits)
    return divmod(best, 60)


# --- clause: main :: () -> None ---
def main():
    out = []
    for h, m, alarms in read_input():
        out.append("%d %d" % sleep_time(h, m, alarms))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
