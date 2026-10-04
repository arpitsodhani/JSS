import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    t = tokens[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = tokens[pos]
        pos += 1
        cases.append(tokens[pos:pos + n])
        pos += n
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
    for stride in range(n):
        here = c[(start + stride) % n]
        nxt = c[(start + stride + 1) % n]
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
