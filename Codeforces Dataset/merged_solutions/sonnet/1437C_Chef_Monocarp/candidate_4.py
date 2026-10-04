import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    q = data[0]
    pos = 1
    cases = []
    for _ in range(q):
        n = data[pos]
        pos += 1
        cases.append(data[pos:pos + n])
        pos += n
    return cases


# --- clause: least_unpleasant :: (times: list[int]) -> int ---
def least_unpleasant(times):
    order = sorted(times)
    n = len(order)
    big = 1 << 30
    best = [0] + [big] * n
    for minute in range(1, 2 * n + 1):
        limit = n if n < minute else minute
        for taken in range(limit, 0, -1):
            previous = best[taken - 1]
            if previous >= big:
                continue
            candidate = previous + abs(minute - order[taken - 1])
            if candidate < best[taken]:
                best[taken] = candidate
    return best[n]


# --- clause: main :: () -> None ---
def main():
    out = []
    for times in read_input():
        out.append(str(least_unpleasant(times)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
