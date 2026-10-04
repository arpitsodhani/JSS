import sys


# --- clause: read_input :: () -> list[tuple[int, int, list[tuple[int, int]]]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    t = tokens[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = tokens[pos]
        h = tokens[pos + 1]
        m = tokens[pos + 2]
        pos += 3
        alarms = []
        for _ in range(n):
            alarms.append((tokens[pos], tokens[pos + 1]))
            pos += 2
        cases.append((h, m, alarms))
    return cases


# --- clause: sleep_time :: (h: int, m: int, alarms: list[tuple[int, int]]) -> tuple[int, int] ---
def sleep_time(h, m, alarms):
    bed = h * 60 + m
    top = 24 * 60
    for hour, minute in alarms:
        wait = (hour * 60 + minute - bed) % (24 * 60)
        if wait < top:
            top = wait
    return top // 60, top % 60


# --- clause: main :: () -> None ---
def main():
    out = []
    for h, m, alarms in read_input():
        out.append("%d %d" % sleep_time(h, m, alarms))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
