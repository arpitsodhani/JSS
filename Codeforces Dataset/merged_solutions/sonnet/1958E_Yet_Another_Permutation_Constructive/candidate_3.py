import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    cases = []
    pos = 1
    for _ in range(t):
        cases.append((data[pos], data[pos + 1]))
        pos += 2
    return cases

# --- clause: build :: (values: list[int], k: int) -> list[int] ---
def build(values, k):
    if k == 1:
        return list(values)
    total = len(values)
    keep = 2 ** (k - 2) + 1
    top = values[total - keep:]
    rest = values[:total - keep]
    survivors = build(top, k - 1)
    separators = rest[-(keep - 1):] if keep > 1 else []
    prefix = rest[:len(rest) - len(separators)]
    result = list(prefix)
    for index, survivor in enumerate(survivors):
        result.append(survivor)
        if index < len(separators):
            result.append(separators[index])
    return result

# --- clause: solve_case :: (n: int, k: int) -> str ---
def solve_case(n, k):
    if (1 << (k - 1)) >= n:
        return "-1"
    return " ".join(map(str, build(list(range(1, n + 1)), k)))


# --- clause: main :: () -> None ---
def main():
    out = []
    for n, k in read_input():
        out.append(solve_case(n, k))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
