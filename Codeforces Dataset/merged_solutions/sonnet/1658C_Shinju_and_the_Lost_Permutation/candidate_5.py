import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    t = raw[0]
    offset = 1
    cases = []
    for _ in range(t):
        n = raw[offset]
        offset += 1
        cases.append(raw[offset:offset + n])
        offset += n
    return cases


# --- clause: is_possible :: (c: list[int]) -> bool ---
def is_possible(c):
    n = len(c)
    start = -1
    ones = 0
    for i in range(n):
        if c[i] == 1:
            ones += 1
            start = i
    if ones != 1:
        return False
    for advance in range(n):
        here = c[(start + advance) % n]
        nxt = c[(start + advance + 1) % n]
        if nxt - here > 1:
            return False
    return True


# --- clause: main :: () -> None ---
def main():
    out = []
    for c in read_input():
        out.append("YES" if is_possible(c) else "NO")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
