import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    pos = 0
    t = int(data[pos])
    pos += 1
    cases = []
    for _ in range(t):
        h = int(data[pos])
        pos += 1
        p = int(data[pos])
        pos += 1
        cases.append((h, p))
    return cases


# --- clause: solve_case :: (h: int, p: int) -> int ---
def solve_case(h, p):
    level = 0
    while level < h and (1 << level) <= p:
        level += 1
    done = (1 << level) - 1
    left = (1 << h) - 1 - done
    return level + (left + p - 1) // p


# --- clause: main :: () -> None ---
def main():
    out = []
    for h, p in read_input():
        out.append(str(solve_case(h, p)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
