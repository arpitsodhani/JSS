import sys


# --- clause: read_input :: () -> list[tuple[int, int, int, int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        cases.append((data[pos], data[pos + 1], data[pos + 2], data[pos + 3]))
        pos += 4
    return cases


# --- clause: solve_case :: (n: int, k: int, b: int, s: int) -> str ---
def solve_case(n, k, b, s):
    low = k * b
    high = low + n * (k - 1)
    if s < low or s > high:
        return "-1"
    arr = [0] * n
    head = min(s, low + k - 1)
    arr[0] = head
    rest = s - head
    for i in range(1, n):
        take = min(k - 1, rest)
        arr[i] = take
        rest -= take
    return " ".join(map(str, arr))


# --- clause: main :: () -> None ---
def main():
    out = []
    for n, k, b, s in read_input():
        out.append(solve_case(n, k, b, s))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
