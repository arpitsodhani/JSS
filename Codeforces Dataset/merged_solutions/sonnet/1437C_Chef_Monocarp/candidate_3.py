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
    big = float("inf")
    best = [big] * (n + 1)
    best[0] = 0
    minute = 1
    while minute <= 2 * n:
        taken = n
        while taken >= 1:
            earlier = best[taken - 1]
            if earlier < big:
                cost = earlier + abs(minute - order[taken - 1])
                if cost < best[taken]:
                    best[taken] = cost
            taken -= 1
        minute += 1
    return int(best[n])


# --- clause: main :: () -> None ---
def main():
    out = []
    for times in read_input():
        out.append(str(least_unpleasant(times)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
