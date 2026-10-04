import sys


# --- clause: read_input :: () -> list[tuple[int, int, int]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    t = raw[0]
    cases = []
    for i in range(t):
        cases.append((raw[1 + 3 * i], raw[2 + 3 * i], raw[3 + 3 * i]))
    return cases


# --- clause: build_sum :: (n: int, k: int, x: int) -> list[int] | None ---
def build_sum(n, k, x):
    if x != 1:
        return [1] * n
    if k < 2:
        return None
    if n % 2 == 0:
        return [2] * (n // 2)
    if k < 3:
        return None
    return [3] + [2] * ((n - 3) // 2)


# --- clause: main :: () -> None ---
def main():
    written = []
    for n, k, x in read_input():
        parts = build_sum(n, k, x)
        if parts is None:
            written.append("NO")
        else:
            written.append("YES")
            written.append(str(len(parts)))
            written.append(" ".join(map(str, parts)))
    sys.stdout.write("\n".join(written) + "\n")


if __name__ == "__main__":
    main()
