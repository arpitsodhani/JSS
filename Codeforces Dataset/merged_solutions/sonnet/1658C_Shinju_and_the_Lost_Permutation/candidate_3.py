import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    t = fields[0]
    cursor = 1
    cases = []
    for _ in range(t):
        n = fields[cursor]
        cursor += 1
        cases.append(fields[cursor:cursor + n])
        cursor += n
    return cases


# --- clause: is_possible :: (c: list[int]) -> bool ---
def is_possible(c):
    n = len(c)
    if c.count(1) != 1:
        return False
    rotated = c[c.index(1):] + c[:c.index(1)]
    for i in range(n - 1):
        if rotated[i + 1] - rotated[i] > 1:
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
