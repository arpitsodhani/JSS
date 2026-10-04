import sys


# --- clause: read_input :: () -> list[tuple[int, int, list[int]]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    pos = 0
    t = int(data[pos])
    pos += 1
    cases = []
    for _ in range(t):
        n = int(data[pos])
        k = int(data[pos + 1])
        pos += 2
        values = [int(data[pos + i]) for i in range(n)]
        pos += n
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
        if counts[value] == 1 and value < whole:
            result[i] = value
        else:
            result[i] = whole
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
            if left % 2 == 0:
                seen = nxt
            else:
                seen = mexify(n, nxt)
            return sum(seen)
        previous = seen
        seen = nxt
    return sum(seen)


# --- clause: main :: () -> None ---
def main():
    out = []
    for case in read_input():
        out.append(str(solve_case(case[0], case[1], case[2])))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
