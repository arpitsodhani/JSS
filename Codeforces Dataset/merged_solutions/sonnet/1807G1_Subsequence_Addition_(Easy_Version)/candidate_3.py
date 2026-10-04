import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    t = fields[0]
    offset = 1
    cases = []
    for _ in range(t):
        n = fields[offset]
        offset += 1
        cases.append(fields[offset:offset + n])
        offset += n
    return cases


# --- clause: can_build :: (c: list[int]) -> bool ---
def can_build(c):
    ranked = sorted(c)
    if ranked[0] != 1:
        return False
    reached = 1
    for i in range(1, len(ranked)):
        if ranked[i] > reached:
            return False
        reached += ranked[i]
    return True


# --- clause: main :: () -> None ---
def main():
    out = []
    for c in read_input():
        out.append("YES" if can_build(c) else "NO")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
