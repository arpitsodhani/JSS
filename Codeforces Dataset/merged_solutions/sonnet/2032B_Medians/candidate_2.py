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


# --- clause: split_points :: (n: int, k: int) -> list[int] | None ---
def split_points(n, k):
    if n == 1:
        if k == 1:
            return [1]
        return None
    if k <= 1 or k >= n:
        return None
    if k & 1:
        return [1, k - 1, k + 2]
    return [1, k, k + 1]


# --- clause: main :: () -> None ---
def main():
    out = []
    for n, k in read_input():
        starts = split_points(n, k)
        if starts is None:
            out.append("-1")
        else:
            out.append(str(len(starts)))
            out.append(" ".join(map(str, starts)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
