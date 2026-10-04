import sys


# --- clause: read_input :: () -> list[tuple[int, int, int, str]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    pos = 0
    t = int(data[pos])
    pos += 1
    cases = []
    for _ in range(t):
        n = int(data[pos])
        x = int(data[pos + 1])
        k = int(data[pos + 2])
        s = data[pos + 3].decode()
        pos += 4
        cases.append((n, x, k, s))
    return cases


# --- clause: first_zero_time :: (start: int, s: str) -> int ---
def first_zero_time(start, s):
    pos = start
    for i in range(len(s)):
        pos += 1 if s[i] == "R" else -1
        if pos == 0:
            return i + 1
    return -1


# --- clause: solve_case :: (n: int, x: int, k: int, s: str) -> int ---
def solve_case(n, x, k, s):
    first = first_zero_time(x, s)
    if first < 0 or first > k:
        return 0
    cycle = first_zero_time(0, s)
    if cycle < 0:
        return 1
    return 1 + (k - first) // cycle


# --- clause: main :: () -> None ---
def main():
    out = []
    for n, x, k, s in read_input():
        out.append(str(solve_case(n, x, k, s)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
