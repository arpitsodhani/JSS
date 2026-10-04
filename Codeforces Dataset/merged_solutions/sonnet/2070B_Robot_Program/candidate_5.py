import sys


# --- clause: read_input :: () -> list[tuple[int, int, int, str]] ---
def read_input():
    raw = sys.stdin.buffer.read().split()
    p = 0
    t = int(raw[p])
    p += 1
    cases = []
    for _ in range(t):
        n = int(raw[p])
        x = int(raw[p + 1])
        k = int(raw[p + 2])
        s = raw[p + 3].decode()
        p += 4
        cases.append((n, x, k, s))
    return cases


# --- clause: first_zero_time :: (start: int, s: str) -> int ---
def first_zero_time(start, s):
    at = start
    for i in range(len(s)):
        if s[i] == "R":
            at = at + 1
        else:
            at = at - 1
        if at == 0:
            return i + 1
    return -1


# --- clause: solve_case :: (n: int, x: int, k: int, s: str) -> int ---
def solve_case(n, x, k, s):
    reach = first_zero_time(x, s)
    if reach < 0:
        return 0
    if reach > k:
        return 0
    repeat = first_zero_time(0, s)
    if repeat < 0:
        return 1
    return 1 + (k - reach) // repeat


# --- clause: main :: () -> None ---
def main():
    out = []
    for case in read_input():
        out.append(str(solve_case(case[0], case[1], case[2], case[3])))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
