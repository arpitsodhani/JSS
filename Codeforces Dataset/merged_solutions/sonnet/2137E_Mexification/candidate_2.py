import sys


# --- clause: read_input :: () -> list[tuple[int, int, list[int]]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    idx = 1
    t = int(data[0])
    cases = []
    for _ in range(t):
        n, k = int(data[idx]), int(data[idx + 1])
        idx += 2
        values = list(map(int, data[idx:idx + n]))
        idx += n
        cases.append((n, k, values))
    return cases


# --- clause: mexify :: (n: int, values: list[int]) -> list[int] ---
def mexify(n, values):
    counts = [0] * (n + 2)
    for value in values:
        counts[value] += 1
    whole = 0
    while whole <= n and counts[whole] > 0:
        whole += 1
    result = [0] * n
    for i in range(n):
        value = values[i]
        if counts[value] != 1 or value >= whole:
            result[i] = whole
        else:
            result[i] = value
    return result


# --- clause: solve_case :: (n: int, k: int, values: list[int]) -> int ---
def solve_case(n, k, values):
    seen = list(values)
    previous = None
    steps = 0
    while steps < k:
        nxt = mexify(n, seen)
        steps += 1
        if nxt == seen:
            break
        if previous is not None and nxt == previous:
            left = k - steps
            if left % 2 == 1:
                seen = mexify(n, nxt)
            else:
                seen = nxt
            return sum(seen)
        previous = seen
        seen = nxt
    return sum(seen)


# --- clause: main :: () -> None ---
def main():
    out = []
    for n, k, values in read_input():
        out.append(str(solve_case(n, k, values)))
    sys.stdout.write("%s\n" % "\n".join(out))


if __name__ == "__main__":
    main()
