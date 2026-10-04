import sys


# --- clause: read_input :: () -> list[tuple[int, int, int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    cases = []
    for i in range(t):
        cases.append((data[1 + 3 * i], data[2 + 3 * i], data[3 + 3 * i]))
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
    out = []
    for n, k, x in read_input():
        parts = build_sum(n, k, x)
        if parts is None:
            out.append("NO")
        else:
            out.append("YES")
            out.append(str(len(parts)))
            out.append(" ".join(map(str, parts)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
