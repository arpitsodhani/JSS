import sys


# --- clause: read_input :: () -> list[tuple[int, int, int, str]] ---
def read_input():
    fields = sys.stdin.buffer.read().split()
    cursor = 0
    total = int(fields[cursor])
    cursor += 1
    cases = []
    while len(cases) < total:
        n = int(fields[cursor])
        x = int(fields[cursor + 1])
        k = int(fields[cursor + 2])
        s = fields[cursor + 3].decode()
        cursor += 4
        cases.append((n, x, k, s))
    return cases


# --- clause: first_zero_time :: (start: int, s: str) -> int ---
def first_zero_time(start, s):
    place = start
    moment = -1
    for i in range(len(s)):
        place += 1 if s[i] == "R" else -1
        if place == 0:
            moment = i + 1
            break
    return moment


# --- clause: solve_case :: (n: int, x: int, k: int, s: str) -> int ---
def solve_case(n, x, k, s):
    entry = first_zero_time(x, s)
    if entry < 0 or k < entry:
        return 0
    again = first_zero_time(0, s)
    if again < 0:
        return 1
    return (k - entry) // again + 1


# --- clause: main :: () -> None ---
def main():
    cases = read_input()
    out = []
    for i in range(len(cases)):
        n, x, k, s = cases[i]
        out.append(str(solve_case(n, x, k, s)))
    print("\n".join(out))


if __name__ == "__main__":
    main()
