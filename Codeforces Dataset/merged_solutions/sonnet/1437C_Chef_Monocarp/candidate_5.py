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
    best = [big] * (n + 1)
    best[0] = 0
    for minute in range(1, 2 * n + 1):
        for taken in range(n, 0, -1):
            earlier = best[taken - 1]
            if earlier == big:
                continue
            gap = minute - order[taken - 1]
            if gap < 0:
                gap = -gap
            if earlier + gap < best[taken]:
                best[taken] = earlier + gap
    return best[n]


# --- clause: main :: () -> None ---
def main():
    out = []
    for times in read_input():
        out.append(str(least_unpleasant(times)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
