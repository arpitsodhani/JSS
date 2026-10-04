import sys


# --- clause: read_input :: () -> list[tuple[int, int, list[tuple[int, int]]]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    t = fields[0]
    cursor = 1
    cases = []
    for _ in range(t):
        n = fields[cursor]
        h = fields[cursor + 1]
        m = fields[cursor + 2]
        cursor += 3
        alarms = []
        for _ in range(n):
            alarms.append((fields[cursor], fields[cursor + 1]))
            cursor += 2
        cases.append((h, m, alarms))
    return cases


# --- clause: sleep_time :: (h: int, m: int, alarms: list[tuple[int, int]]) -> tuple[int, int] ---
def sleep_time(h, m, alarms):
    bed = h * 60 + m
    peak = 24 * 60
    for hour, minute in alarms:
        wait = (hour * 60 + minute - bed) % (24 * 60)
        if wait < peak:
            peak = wait
    return peak // 60, peak % 60


# --- clause: main :: () -> None ---
def main():
    out = []
    for h, m, alarms in read_input():
        out.append("%d %d" % sleep_time(h, m, alarms))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
