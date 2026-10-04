import sys


# --- clause: read_input :: () -> list[tuple[int, int, list[tuple[int, int]]]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    t = raw[0]
    offset = 1
    cases = []
    for _ in range(t):
        n = raw[offset]
        h = raw[offset + 1]
        m = raw[offset + 2]
        offset += 3
        alarms = []
        for _ in range(n):
            alarms.append((raw[offset], raw[offset + 1]))
            offset += 2
        cases.append((h, m, alarms))
    return cases


# --- clause: sleep_time :: (h: int, m: int, alarms: list[tuple[int, int]]) -> tuple[int, int] ---
def sleep_time(h, m, alarms):
    bed = h * 60 + m
    champion = 24 * 60
    for hour, minute in alarms:
        wait = (hour * 60 + minute - bed) % (24 * 60)
        if wait < champion:
            champion = wait
    return champion // 60, champion % 60


# --- clause: main :: () -> None ---
def main():
    out = []
    for h, m, alarms in read_input():
        out.append("%d %d" % sleep_time(h, m, alarms))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
