import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    pos = 1
    t = int(data[0])
    cases = []
    while len(cases) < t:
        h = int(data[pos])
        p = int(data[pos + 1])
        pos += 2
        cases.append((h, p))
    return cases


# --- clause: solve_case :: (h: int, p: int) -> int ---
def solve_case(h, p):
    level = 0
    while level < h:
        if (1 << level) > p:
            break
        level += 1
    left = (1 << h) - (1 << level)
    return level + (left + p - 1) // p


# --- clause: main :: () -> None ---
def main():
    out = []
    for pair in read_input():
        out.append(str(solve_case(pair[0], pair[1])))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
